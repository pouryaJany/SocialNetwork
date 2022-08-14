from django import forms


class RegistrationUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'pourya'}))

    email = forms.EmailField()
    password = forms.CharField()
