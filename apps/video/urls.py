from django.urls import path
from apps.video import views

urlpatterns = [
    path('video/<videoId>/', views.VideoAppList.as_view()),
    path('', views.VideoAppList.as_view())
]