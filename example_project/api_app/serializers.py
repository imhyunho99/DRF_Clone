from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)  # ID가 자동으로 들어가게 설정
    author_name = serializers.CharField(write_only=True)  # 입력 전용 필드

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name']  # author_name 필드 추가

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')  # 입력된 author_name 가져오기
        author, created = Author.objects.get_or_create(name=author_name)  # 없으면 생성
        validated_data['author'] = author  # Book과 연결
        return super().create(validated_data)
