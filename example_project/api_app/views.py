from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST']) #url : /create body { title, author, publication_date, price }
@permission_classes([AllowAny])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET']) #url : /list
@permission_classes([AllowAny])
def get_books(request):
    data = BookSerializer.read()
    return Response(data)


@api_view(['POST']) #url : /delete body { id }
@permission_classes([AllowAny])
def delete_book(request):
    book_id = request.data.get('id')  # POST body 'id':

    if not book_id:
        return Response({"error": "Book id is required"}, status=400)

    success = BookSerializer.delete(book_id)
    if success:
        return Response({"message": "Book deleted"}, status=200)
    return Response({"error": "Book not found"}, status=404)


@api_view(['POST']) #url : /delete body { id, title, author, publication_date, price }
@permission_classes([AllowAny])
def update_book(request):
    book_id = request.data.get('id')
    if not book_id:
        return Response({"error": "Book id is required"}, status=400)

    update_data = request.data.copy()
    update_data.pop('id', None)

    updated = BookSerializer.update(book_id, update_data)
    if updated:
        return Response(updated, status=200)
    return Response({"error": "Book not found"}, status=404)
