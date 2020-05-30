"""django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("post.urls"), name="posts"),
    url(r'^api/posts/', include("post.api.urls"), name="posts-api"),
    url(r'^api/comments/', include("comments.api.urls"), name="comments-api")
    # url(r'^api/auth/', include('rest_auth.urls')),
    # url(r'^api/auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^accounts/', include('allauth.urls')),

]

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
