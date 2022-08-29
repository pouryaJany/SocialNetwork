from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('all-post/', views.ShowAllPost.as_view(), name='all-post')
]
