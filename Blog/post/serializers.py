from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Comment

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Post serializer


class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body_text', 'published_date']


class ListPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    title = serializers.CharField(source='formatTitle')
    published_date = serializers.ReadOnlyField(source='formatDate')
    class Meta:
        model = Post
        fields = ['id', 'author', 'title',
                  'body_text', 'published_date']

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',]

# Comment serializer

class DeleteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',]

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content',]

class ListCommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.StringRelatedField()
    published_date = serializers.ReadOnlyField(source='formatDate')
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'content',
            'published_date'
        ]
