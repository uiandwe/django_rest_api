__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from post.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment

class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at'
        ]

    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at',
            'comments',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_comments(self, obj):
        c_qs = Comment.objects.filter(post=obj.id, parent_comment__isnull=True)
        comments = CommentSerializer(c_qs, many=True).data
        return comments


class PostSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
