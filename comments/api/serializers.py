__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'parent_comment',
            'content',
            'timestamp',

        ]

