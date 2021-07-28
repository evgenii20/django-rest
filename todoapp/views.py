from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer

# Create your views here.


# Create your views here.
# namespace = 'todoapp'


class ProjectModelViewSet(ModelViewSet):
    # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
    # моделью и будет работать с её данными.
    # serializer_class определяет тот Serializer, который мы будем использовать.
    # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProjectModelSerializer
    # queryset указывает, какие данные мы будем выводить в списке.
    queryset = Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
