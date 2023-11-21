from django.urls import path
from apps.video import views

urlpatterns = [
    path('video/<int:videoId>/', views.VideoDetailView.as_view()),
    path('', views.VideoAppList.as_view())
]
