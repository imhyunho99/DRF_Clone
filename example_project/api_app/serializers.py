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
