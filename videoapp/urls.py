from django.urls import path
from videoapp import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
    path('search/', views.search_videos, name='search_videos'),
]