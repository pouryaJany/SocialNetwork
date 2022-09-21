from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationUserForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Post

# Create your views here.


class RegisterUserView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def get(request):
        form = RegistrationUserForm()
        context = {
            'form': form
        }
        return render(request, 'account/register_page.html', context)

    @staticmethod
    def post(request):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"], cd["email"], cd["password1"])
            messages.success(request, "you registered successfully", "success")
            return redirect('home:home')
        else:
            return render(request, 'account/register_page.html', {'form': form})


class LoginUserView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'account/login_page.html', context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                messages.success(request, "you logged in successfully", "success")
                login(request, user)
                return redirect('home:home')
            else:
                messages.error(request, "invalid username or password", "danger")
                return redirect('account:login')


class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "you logged out successfully", "success")
        return redirect('account:login')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(user=user)
        context = {
            'web_user': user,
            'posts': posts
        }
        return render(request, 'account/profile.html', context)
