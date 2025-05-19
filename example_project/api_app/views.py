from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import status


"""
ViewSet
"""
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes([AllowAny])



"""
Serializer
"""

@api_view(['POST'])  # /create
@permission_classes([AllowAny])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])  # /list
@permission_classes([AllowAny])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])  # /delete
@permission_classes([AllowAny])
def delete_book(request):
    book_id = request.data.get('id')
    if not book_id:
        return Response({"error": "Book id is required"}, status=400)

    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({"message": "Book deleted"}, status=200)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)


@api_view(['POST'])  # /update
@permission_classes([AllowAny])
def update_book(request):
    book_id = request.data.get('id')
    if not book_id:
        return Response({"error": "Book id is required"}, status=400)

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    update_data = request.data.copy()
    update_data.pop('id', None)

    serializer = BookSerializer(book, data=update_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)
        response = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response)
