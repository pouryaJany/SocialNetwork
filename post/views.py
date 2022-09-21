import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import View
from .models import Post, Image
from .forms import PostUpdateForm, PostImageUpdateForm, PostCreationForm, ImageSelectionForPostCreationForm


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


class DeletePost(View):
    @staticmethod
    def get(request, post_id):
        post = Post.objects.get(id=post_id)
        image = Image.objects.get(post=post)
        post.delete()
        image.delete()
        return redirect("account:profile", user_id=request.user.id)


class UpdatePost(View):
    form_class = PostUpdateForm

    @staticmethod
    def get(request, post_id):
        post = Post.objects.get(pk=post_id)
        image = Image.objects.get(post=post)
        form1 = PostUpdateForm(instance=post)
        form2 = PostImageUpdateForm(instance=image)
        context = {
            'form1': form1,
            'form2': form2
        }
        return render(request, 'post/update_post.html', context)

    @staticmethod
    def post(request, post_id):
        post = Post.objects.get(id=post_id)
        image = Image.objects.get(post=post)
        form1 = PostUpdateForm(request.POST, instance=post)
        form2 = PostImageUpdateForm(request.POST, request.FILES, instance=image)
        if form1.is_valid():
            new_post = form1.save(commit=False)
            new_post.slug = slugify(form1.cleaned_data['title'])
            if form2.is_valid():
                img = Image.objects.create(image1=form2.cleaned_data["image1"], image2=form2.cleaned_data["image2"],
                                           image3=form2.cleaned_data["image3"], image4=form2.cleaned_data["image4"],
                                           image5=form2.cleaned_data["image5"])
                new_post.image = img
                new_post.save()
                messages.success(request, "you updated this post successfully", "success")
                return redirect("post:detail-post", post_id, new_post.slug)
            else:
                raise ValueError("alisuhfksjdf")


class CreatePost(View):
    @staticmethod
    def get(request):
        form1 = PostCreationForm()
        form2 = ImageSelectionForPostCreationForm()
        context = {
            'form1': form1,
            'form2': form2
        }
        return render(request, 'post/create_post.html', context)

    @staticmethod
    def post(request):
        form1 = PostCreationForm(request.POST)
        form2 = ImageSelectionForPostCreationForm(request.POST, request.FILES)
        if form1.is_valid():
            cd_of_form1 = form1.cleaned_data
            if form2.is_valid():
                cd_of_form2 = form2.cleaned_data
                img = Image.objects.create(image1=cd_of_form2["image1"], image2=cd_of_form2["image2"],
                                           image3=cd_of_form2["image3"], image4=cd_of_form2["image4"],
                                           image5=cd_of_form2["image5"])
                post = Post.objects.create(title=cd_of_form1["title"], caption=cd_of_form1["caption"]
                                           , image=img, user=request.user, slug=slugify(cd_of_form1["title"]))
                messages.success(request, "you created this post successfully")
                return redirect("account:profile", request.user.id)
