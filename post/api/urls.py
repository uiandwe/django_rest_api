__author__ = 'uiandwe'

from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostDetailAPIView,
    PostListAPIView,
)


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),


]