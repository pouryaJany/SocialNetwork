from django.shortcuts import render
from django.views import View
from .forms import RegistrationUserForm


# Create your views here.


class RegisterUserView(View):
    def get(self, request):
        form = RegistrationUserForm()
        context = {
            'form': form
        }
        return render(request, 'account/register_page.html', context)
