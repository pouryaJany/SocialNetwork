from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UserProfileView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name='profile'),
]
