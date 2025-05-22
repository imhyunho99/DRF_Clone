from django.urls import include, path
from rest_framework import routers

from .views import (BookViewSet, UserLoginView, UserRegistrationView,
                    create_book, delete_book, get_books, update_book)

router = routers.DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("create/", create_book, name="create_book"),
    path("list/", get_books, name="get_books"),
    path("delete/", delete_book, name="delete_book"),
    path("update/", update_book, name="update_book"),
]
