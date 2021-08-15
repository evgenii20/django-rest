from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from .views import APIUserView
from userapp.models import APIUser


# Create your tests here.

class TestAPIUserViewSet(TestCase):
    """интеграционные тесты тестируют всю бизнес логику"""
    URL = '/api/users/'

    # def setUp(self):
    #     factory = APIRequestFactory()
    #     self.request = factory.get(self.URL)

    def test_get_list(self):
        # будет проверять страницу со списком пользователей
        # APIRequestFactory — фабрика для создания запросов, используется для специфичных тестов низкого уровня;
        factory = APIRequestFactory()
        admin = APIUser.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
        # request = factory.get('/api/authors/')
        # request = factory.get('/api/users/')
        request = factory.get(self.URL)
        force_authenticate(request, admin)
        view = APIUserView.as_view({'get': 'list'})
        # response = view(request)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        factory = APIRequestFactory()
        request = factory.post(self.URL, {
            'username': 'django2',
            'first_name': 'Семён',
            'last_name': 'Семёнов',
            'email': 'django2@django.ru'
        }, format='json')
        # view = APIUserView.as_view({'post': 'update'})
        view = APIUserView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user(self):
        factory = APIRequestFactory()
        # создаём суперпользователя
        admin = APIUser.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
        request = factory.post(self.URL, {
            'username': 'django2',
            'first_name': 'Семён',
            'last_name': 'Семёнов',
            'email': 'django2@django.ru'
        }, format='json')
        force_authenticate(request, admin)
        # view = APIUserView.as_view({'post': 'update'})
        view = APIUserView.as_view({'post': 'create'})
        response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
