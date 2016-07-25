__author__ = 'uiandwe'
from rest_framework.generics import ListAPIView, RetrieveAPIView

from post.models import Post
from post.api.serializers import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer