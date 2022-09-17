from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('all-post/', views.ShowAllPost.as_view(), name='all-post'),
    path('detail-post/<int:id>/<slug:slug>/', views.ShowDetailPost.as_view(), name='detail-post'),
    path('delete-post/<int:post_id>/', views.DeletePost.as_view(), name='delete-post')
]
