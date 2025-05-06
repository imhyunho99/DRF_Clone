from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_name = validated_data.pop('author')
        author, _ = Author.objects.get_or_create(name=author_name, defaults={'age': None})
        return Book.objects.create(author=author, **validated_data)

    def update(self, instance, validated_data):
        author_name = validated_data.pop('author', None)
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name, defaults={'age': None})
            instance.author = author

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
