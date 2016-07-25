__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer
from post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'content',
            'created_at',
        ]