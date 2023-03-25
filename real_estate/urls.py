from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import (
    LogInUserView,
    LogOutUserView,
    RegisterUserView,
    UserListCreateView,
    UserRetrieveUpdateDestroy,
)
from django.urls import path


# user defined routes

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LogInUserView.as_view(), name="login"),
    path("logout/", LogOutUserView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("token/create/", TokenObtainPairView.as_view(), name="create-token"),
    path("", UserListCreateView.as_view(), name="create"),
    path("<int:pk>/", UserRetrieveUpdateDestroy.as_view(), name="users"),
]
