__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    child_comments = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'content',
            'timestamp',
            'child_comments',

        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_child_comments(self, obj):
        c_qs = Comment.objects.filter(parent_comment=obj.id)
        comments = CommentSerializer(c_qs, many=True).data
        return comments