from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, permissions, serializers, status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import *


# Post List
class PostListApiView(ListAPIView):
    serializer_class = ListPostSerializer
    queryset = Post.objects.all().order_by('-id')


class AddPost(CreateAPIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = AddPostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        author = User.objects.get(id=self.request.user.id)
        serializer.save(author=author)


class ShowPost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    lookup_field = 'id'


class MyPosts(ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Post.objects.all().filter(author=author).order_by('-id')


class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = DeletePostSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

# Comment

class CommentList(ListAPIView):
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        post = self.kwargs['post']
        return Comment.objects.all().filter(post=post).order_by('-id')


class AddComment(CreateAPIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = AddCommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        author = User.objects.get(id=self.request.user.id)
        serializer.save(author=author)


class DeleteComment(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = DeleteCommentSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)