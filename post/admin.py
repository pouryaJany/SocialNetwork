from django.contrib import admin
from .models import Post, Image


# Register your models here.
admin.site.register(Image)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "user", "created", "is_puplished")
    list_filter = ("created",)
