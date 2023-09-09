from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .entity import HomePageCtx
from .models import BlogPost
from mailing.models import Client, EmailSchedule


class HomeView(View):
    template_name = "blog/home.html"

    def get(self, request):
        ctx = HomePageCtx(
            total_mailings=EmailSchedule.objects.count(),
            active_mailings=EmailSchedule.objects.filter(status="running").count(),
            random_posts=BlogPost.objects.order_by("?")[:3],
            unique_clients=Client.objects.distinct("email").count(),
        )

        return render(request, self.template_name, context={"ctx": ctx})


class PostDetailView(DetailView):
    model = BlogPost
    context_object_name = "blog_post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()

        return obj


class PublishedPostsListView(ListView):
    model = BlogPost
    context_object_name = "all_posts"

    def get_queryset(self):
        """
        Return only is_published = True
        """
        return super().get_queryset().filter(is_published=True)
