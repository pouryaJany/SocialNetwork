from django import forms


class RegistrationUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
