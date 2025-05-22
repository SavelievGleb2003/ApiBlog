from django.urls import path
from posts.views import PostList, PostDetail, UserDetail, UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_datail'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list')
]
