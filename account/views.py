from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationUserForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


class RegisterUserView(View):
    def get(self, request):
        form = RegistrationUserForm()
        context = {
            'form': form
        }
        return render(request, 'account/register_page.html', context)

    def post(self, request):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"], cd["email"], cd["password1"])
            messages.success(request, "you registered successfully", "success")
            return redirect('home:home')
        else:
            return render(request, 'account/register_page.html', {'form': form})


class LoginUserView(View):
    def get(self, request):
        return render(request, 'account/login_page.html')

    def post(self, request):
        pass
