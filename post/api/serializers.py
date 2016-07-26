__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from post.models import Post


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='pk'
    )

    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='pk'
    )

    update_url = HyperlinkedIdentityField(
        view_name='posts-api:update',
        lookup_field='pk'
    )
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at',
            'url',
            'update_url',
            'delete_url'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

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