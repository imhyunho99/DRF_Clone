from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField()  # 문자열로 직접 받음

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_name = validated_data.pop('author')  # 문자열 꺼내기

        # Author 없으면 생성 (age=None)
        author, created = Author.objects.get_or_create(
            name=author_name,
            defaults={'age': None}
        )

        # Book 생성
        book = Book.objects.create(author=author, **validated_data)
        return book

    @classmethod
    def read(cls):
        books = Book.objects.all()
        return cls(books, many=True).data

    @classmethod
    def delete(cls, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return True
        except Book.DoesNotExist:
            return False

    @classmethod
    def update(cls, book_id, data):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None  # view에서 처리할 수 있도록

        author_name = data.pop('author', None)
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name, defaults={'age': None})
            book.author = author

        for attr, value in data.items():
            setattr(book, attr, value)

        book.save()
        return cls(book).data
