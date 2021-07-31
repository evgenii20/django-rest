from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# from .filters import ProjectListAPIView
from .filters import ProjectFilter, TodoFilter
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


# Create your views here.


# Create your views here.
# namespace = 'todoapp'


# class ProjectModelViewSet(ModelViewSet):
#     # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
#     # моделью и будет работать с её данными.
#     # serializer_class определяет тот Serializer, который мы будем использовать.
#     # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
#     # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     serializer_class = ProjectModelSerializer
#     # queryset указывает, какие данные мы будем выводить в списке.
#     queryset = Project.objects.all()
# filterset_fields = ProjectFilter

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_backends = [filters.OrderingFilter]
    pagination_class = ProjectLimitOffsetPagination

    # filterset_fields = ProjectListAPIView
    # filterset_fields = ProjectFilter

    # @action(methods=['GET'], detail=True)
    def get_queryset(self):
        # name = self.request.query_params.get('name', None)
        name = self.request.query_params.get(ProjectFilter, None)
        # articles = Article.objects.all()
        projects = Project.objects.all()
        if name:
            # projects = projects.filter(name__contains=name)
            return projects.filter(name__contains=name)
        return projects


# class ProjectCustomFilterViewSet(ModelViewSet):
#    queryset = Project.objects.all()
#    serializer_class = ProjectModelSerializer
#    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    pagination_class = TodoLimitOffsetPagination

    # filterset_fields = TodoFilter

    # @action(methods=['GET'], detail=True)
    # def get_queryset(self):
    #     # name = self.request.query_params.get('name', '')
    #     project = self.request.query_params.get(TodoFilter, None)
    #     # articles = Article.objects.all()
    #     todos = Todo.objects.all()
    #     if todos:
    #         # projects = projects.filter(name__contains=name)
    #         return todos.filter(name__contains=project)
    #     return todos
    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs.get('pk'))
        todo.is_active = 'False'
        todo.save()
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)
