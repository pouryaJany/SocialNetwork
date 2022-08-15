from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'pourya'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'test@test.com'
    }))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("this email is already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("this username is already exists")
        return username

    def clean(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass2 and pass1 and pass1 != pass2:
            raise ValidationError("passwords must be same")


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
