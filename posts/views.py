from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from posts.models import Post
from rest_framework.permissions import IsAdminUser
from posts.permissions import IsAuthorOrReaOnly
from posts.serializers import PostSerializer, UserSerializer
# Create your views here.


class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReaOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReaOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserList(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer