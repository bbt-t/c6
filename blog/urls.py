from django.urls import path

from .views import HomeView, PostDetailView, PublishedPostsListView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("blog/", PublishedPostsListView.as_view(), name="all_posts"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
