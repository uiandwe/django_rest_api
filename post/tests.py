from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from post.api.views import PostDetailAPIView, PostListAPIView
from post.models import Post
from django.contrib.auth.models import User


class AccountTests(APITestCase):
    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.email = 'test@test.test'
        self.name = 'admin'
        self.password = 'uiandwe3'
        user = User.objects.create_user(email=self.email, username=self.name, password=self.password, is_active=True)
        user.save()
        self.data = {
            'email': self.email,
            'password': self.password
        }
        # 처음 생성시 is_Admin이 실행되지 않음(django 정책)
        user.is_admin = True
        user.save()
        self.url = '/api/auth/token/'

    def test_create_account(self):
        u = User.objects.all()
        print(u)
        client = APIClient()
        client.login(username='admin', password='uiandwe3')

        self.client.login(username='admin', password='uiandwe3')
        response = self.client.get('/api/posts/', format='json')
        print(response.data)
        self.assertTrue(response.status_code, 200)

        url = '/api/posts/create/'
        data = {"title": "test", "content": "content"}
        response = client.post(url, data, format='json')
        self.assertEquals(response.data['pk'], 1)

        p = Post.objects.all()
        print(p)
