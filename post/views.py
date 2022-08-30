from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.


class ShowAllPost(View):
    @staticmethod
    def get(request):
        my_posts = Post.objects.filter(is_puplished=True)
        context = {
            'posts': my_posts
        }
        return render(request, 'post/all_post.html', context)


class ShowDetailPost(View):
    @staticmethod
    def get(request, id, slug):
        post = Post.objects.get(id=id, slug=slug)
        images = [post.image.image1, post.image.image2, post.image.image3, post.image.image4, post.image.image5]
        print(images)
        context = {
            'post': post,
            'images': images
        }

        return render(request, 'post/detail_post.html', context)
