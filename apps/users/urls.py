from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('avatar-update/', user_avatar_update, name='user_avatar_update'),
]
