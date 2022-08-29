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

