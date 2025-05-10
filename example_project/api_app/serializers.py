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

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(


            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

