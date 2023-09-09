from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from custom_auth.models import CustomUser


class PostManager(models.Manager):
    """
    BlogPost.manager.is_published() / .manager.not_published()
    """

    def get_queryset(self):
        return super().get_queryset()

    def not_published(self):
        return super().get_queryset().filter(is_published=False)

    def is_published(self):
        return super().get_queryset().filter(is_published=True)


class BlogPost(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(
        max_length=64,
        blank=True,
        unique_for_date="create_at",
        verbose_name="идентификатор",
    )
    title = models.CharField(max_length=128, verbose_name="заголовок")
    content = models.TextField(verbose_name="текст статьи")
    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        verbose_name="картинка",
    )
    views = models.PositiveIntegerField(default=0, verbose_name="просмотры")
    is_published = models.BooleanField(default=False, verbose_name="опубликовано?")
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name="создано"
    )  # or default=timezone.now()

    objects = models.Manager()
    manager = PostManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

        db_table_comment = "Posts for blog app"

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])

    def save(self, *args, **kwargs) -> None:
        if self._state.adding and not self.slug:
            self._generate_slug()
        super().save(*args, **kwargs)

    def _generate_slug(self) -> None:
        if BlogPost.objects.filter(slug=self.slug).exists():
            self.slug = slugify(f"{self.title}_{self.create_at.date()}")
        else:
            self.slug = slugify(self.title)
