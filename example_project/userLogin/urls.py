from django.urls import path

from .views import (DeleteUserView, LoginView, LogoutView, RegisterView,
                    TokenDeleteUserView, TokenLoginView, TokenLogoutView,
                    TokenRegisterView, TokenUserDetailView, UserDetailView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
    path("delete/", DeleteUserView.as_view(), name="user-delete"),
    path("tokenregister/", TokenRegisterView.as_view(), name="tokenregister"),
    path("tokenlogin/", TokenLoginView.as_view(), name="tokenlogin"),
    path("tokenlogout/", TokenLogoutView.as_view(), name="tokenlogout"),
    path("tokenme/", TokenUserDetailView.as_view(), name="tokenuser-detail"),
    path("tokendelete/", TokenDeleteUserView.as_view(), name="tokenuser-delete"),
]
