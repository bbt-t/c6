from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Blog app view in the admin panel.
    """

    list_display = "creator", "title", "content", "image", "views", "create_at"
    ordering = ("create_at",)
    list_filter = ("is_published",)
