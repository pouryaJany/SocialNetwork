from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.


# def home(request):
#     return render(request, 'home/index.html')

class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, 'home/index.html')
