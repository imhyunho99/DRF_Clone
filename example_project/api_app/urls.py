from django.urls import path, include
from .views import create_book, get_books,delete_book, update_book
from rest_framework import routers
from django.urls import path, include
from .views import BookViewSet, UserRegistrationView, UserLoginView


router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', create_book, name='create_book'),
    path('list/', get_books, name='get_books'),
    path('delete/', delete_book, name='delete_book'),
    path('update/', update_book, name='update_book'),
]
