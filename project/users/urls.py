from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, login, get_profile

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("login", login, name="auth"),
    path("register", register, name="auth"),
    path("profile", get_profile, name="auth"),
]
