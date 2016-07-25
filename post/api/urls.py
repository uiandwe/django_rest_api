__author__ = 'uiandwe'

from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView
)


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),

]