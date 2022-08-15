from django.urls import path
from .views import RegisterUserView, LoginUserView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login')
]