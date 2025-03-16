from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import (
    CustomTokenBlacklistView,
    MeView,
    RegisterView,
    UpdatePasswordView,
)

app_name = 'accounts'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('me', MeView.as_view(), name='me'),
    path('update-password', UpdatePasswordView.as_view(), name='update-password'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('logout', CustomTokenBlacklistView.as_view(), name='logout'),
]
