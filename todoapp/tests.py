from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, force_authenticate
from todoapp.models import Todo, Project
# Create your tests here.
from userapp.models import APIUser
from mixer.backend.django import mixer


class TestProjectModel(TestCase):
    """интеграционные тесты тестируют всю бизнес логику"""
    URL = '/api/projects/'

    def test_get_project(self):
        client = APIClient()
        response = client.get(f'{self.URL}')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestTodoModel(TestCase):
    """интеграционные тесты тестируют всю бизнес логику"""
    URL = '/api/todo/'

    # def test_get_detail(self):
    #     user = APIUser.objects.create(username='django2', first_name='Семён', last_name='Семёнов',
    #                                   email='django2@django.ru')
    #     client = APIClient()
    #     # response = client.get('{0}/{1}/'.format(self.URL, user.id))
    #     response = client.get(f'{self.URL}{user.id}/')
    #     # print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # self.assertEqual(response.data.get('first_name'), APIUser.first_name)
    #
    def test_get_todo_admin(self):
        admin = APIUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        # user = APIUser.objects.create(username='django2', first_name='Семён', last_name='Семёнов', email='django2@django.ru')
        client = APIClient()
        # перед отправкой запроса, создаём пользователя и авторизуемся
        client.force_authenticate(admin)
        # client.login(username='admin', password='admin123456')
        response = client.get(self.URL)
        # response = client.post(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверим
        # user = APIUser.objects.get(id=user.id)
        # user = APIUser.objects.get(id=user.id)
        # self.assertEqual(user.fist_name, 'Григорий')
        # self.assertEqual(user.last_name, 'Георгиев')
        client.logout()


class TestProjectModelAPITestCase(APITestCase):
    URL = '/api/projects/'

    def test_get_list(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_project(self):
        # user = APIUser.objects.create(name='user1', email='user1@django.ru')
        project = Project.objects.create(name='Test project name1', text='Тест текста1')
        admin = APIUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        # request = self.client.put(f'{self.URL}{project.id}/', {'name': 'Имя проекта1'})
        # force_authenticate(request, admin)
        # self.client.force_authenticate(request, admin)
        self.client.login(username='admin', password='admin123456')
        # self.client.force_login(username='admin', password='admin123456')
        response = self.client.put(f'{self.URL}{project.id}/', {'name': 'Имя проекта1'})
        # response = self.client.force_authenticate(request, admin)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # # Проверка
        # project = Project.objects.get(id=Project.id)
        # self.assertEqual(project.name, 'Имя проекта1')

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        # user = mixer.blend(User, username='testuser', groups__name='admin')
        admin = APIUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        # response = self.client.put(f'{self.URL}{project.id}/', {'name': 'Test project name1', 'users': project.users.id})
        response = self.client.put(f'{self.URL}{project.id}/', {'name': 'Test project name1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'Имя проекта1')
