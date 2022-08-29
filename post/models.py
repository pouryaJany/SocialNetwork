from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Image(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_puplished = models.BooleanField(default=False)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.slug}'
