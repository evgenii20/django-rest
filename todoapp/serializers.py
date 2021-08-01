from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from todoapp.models import Project, Todo
from userapp.models import APIUser


class APIUserModelSerializer(ModelSerializer):
    class Meta:
        model = APIUser
        fields = '__all__'
        # сериализатор на основании модели User будет создавать JSON-представление
        # при объявлении полей - быть внимательнее! иначе не грузится HTML-форма на странице
        # http://127.0.0.1:8000/api/userapp/
        # fields = ('user_name', 'first_name', 'last_name', 'email')
        # fields = ('id', 'first_name', 'last_name', 'email')
        # fields = ['text', 'author']


class ProjectModelSerializer(ModelSerializer):
    # users = APIUserModelSerializer(APIUser, many=True)
    # users = APIUserModelSerializer(APIUser, many=True)

    class Meta:
        model = Project
        # сериализатор на основании модели Project будет создавать JSON-представление
        fields = '__all__'
        # fields = ('name', 'text', 'users')


class TodoModelSerializer(ModelSerializer):
    # users = APIUserModelSerializer()
    # projects = ProjectFilterModelViewSet()

    class Meta:
        model = Todo
        # сериализатор на основании модели To do будет создавать JSON-представление
        fields = '__all__'
