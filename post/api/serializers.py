__author__ = 'uiandwe'

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
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


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at',
        ]