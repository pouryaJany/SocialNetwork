from django.shortcuts import render
from django.views import View
# Create your views here.


class RegisterUserView(View):
    def get(self, request):
        return render(request, 'account/register_page.html')