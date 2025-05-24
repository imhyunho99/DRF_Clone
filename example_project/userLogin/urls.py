from django.urls import path

from .views import (DeleteUserView, LoginView, LogoutView, RegisterView, UserDetailView,
                    TokenDeleteUserView, TokenLoginView, TokenLogoutView, TokenRegisterView, TokenUserDetailView,
                    JWTDeleteUserView, JWTLoginView, JWTLogoutView, JWTRegisterView, JWTUserDetailView,)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
    path("delete/", DeleteUserView.as_view(), name="user-delete"),
    path("tokenregister/", TokenRegisterView.as_view(), name="token-register"),
    path("tokenlogin/", TokenLoginView.as_view(), name="token-login"),
    path("tokenlogout/", TokenLogoutView.as_view(), name="token-logout"),
    path("tokenme/", TokenUserDetailView.as_view(), name="token-user-detail"),
    path("tokendelete/", TokenDeleteUserView.as_view(), name="token-user-delete"),
    path("jwtregister/", JWTRegisterView.as_view(), name="JWT-register"),
    path("jwtlogin/", JWTLoginView.as_view(), name="JWT-login"),
    path("jwtlogout/", JWTLogoutView.as_view(), name="JWT-logout"),
    path("jwtme/", JWTUserDetailView.as_view(), name="JWT-user-detail"),
    path("jwtdelete/", JWTDeleteUserView.as_view(), name="JWT-user-delete"),
]
