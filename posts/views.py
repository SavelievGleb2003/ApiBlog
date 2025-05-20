from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from posts.models import Post
from posts.permissions import IsAuthorOrReaOnly
from posts.serializers import PostSerializer
# Create your views here.


class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReaOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReaOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer