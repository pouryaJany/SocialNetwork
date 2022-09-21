from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UserProfileView, UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name='profile'),
    path('password-reset/', UserPasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', UserPasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', UserPasswordResetCompleteView.as_view(), name='password-reset-complete')
]
