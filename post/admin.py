from django.contrib import admin
from .models import Post, Image
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
admin.site.register(Image)


@admin.register(Post)
class PostAdmin(BaseUserAdmin):
    prepopulated_fields = {("slug",): ("title",)}
    list_display = ("title", "user", "created", "is_puplished")
    list_filter = ("created",)
