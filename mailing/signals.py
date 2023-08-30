from apscheduler.jobstores.base import JobLookupError
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import EmailSchedule
from .scheduler import scheduler
from .utils import send_emails


def remove_job(job_id: str) -> None:
    """
    Remove job.
    """
    try:
        scheduler.remove_job(job_id)
    except JobLookupError:
        print("Попытка отключения или удаления несуществующей записи ->", job_id)
    else:
        print("Удалено ->", job_id)


@receiver(post_save, sender=EmailSchedule)
def update_sending_configuration(sender, instance: EmailSchedule, **kwargs) -> None:
    """
    Call after saving the model.
    """
    job_id = f"job_for_{instance.pk}"
    print(job_id)
    if instance.status == "running":
        send_time = instance.send_time
        param = {
            "id": job_id,
            "hour": send_time.time().hour,
            "minute": send_time.time().minute,
            "args": (instance.pk,),
        }
        match instance.interval:
            case "weekly":
                param |= {
                    "day_of_week": send_time.strftime("%a").lower(),
                }
            case "monthly":
                param |= {"day": send_time.day}

        if scheduler.get_job(job_id=job_id):
            scheduler.remove_job(job_id=job_id)

        scheduler.add_job(
            send_emails,
            "cron",
            **param,
        )

    elif instance.status == "disabled":
        remove_job(job_id=job_id)


@receiver(pre_delete, sender=EmailSchedule)
def remove_sending_configuration(sender, instance, **kwargs) -> None:
    """
    Call BEFORE deleting the model.
    """
    remove_job(job_id=f"job_for_{instance.pk}")
