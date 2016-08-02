from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    post = models.ForeignKey(Post, null=True, blank=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
