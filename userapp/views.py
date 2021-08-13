from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from .models import APIUser
from .serializers import APIUserModelSerializer
# from .serializers import APIUserSerializer


# Create your views here.
# namespace = 'userapp'

# # Основа
#
# class APIUserView(GenericAPIView):
#     def get_renderers(self):
#       """В зависимости от кода возвращать список рендеров"""
#         # if ():
#         return [JSONRenderer]
#     # renderer_classes = [JSONRenderer]
#
# class APIUserView(APIView):
#     # renderer_classes = [JSONRenderer]
#
#     def get(self, request, format=None):
#         """Создаём свой View, наследуясь от APIView.
#         Метод get отвечает за get-запрос. Мы получаем всех пользователей,
#         с помощью APIUserModelSerializer преобразуем выборку в простые типы данных
#         и возвращаем объект Response. Позволяет формировать REST-API с любым содержимым"""
#         users = APIUser.objects.all()
#         serializer = APIUserSerializer(users, many=True)
#         return Response(serializer.data)

#
# class APIUserModelViewSet(ModelViewSet):
#     # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
#     # моделью и будет работать с её данными.
#     # serializer_class определяет тот Serializer, который мы будем использовать.
#     # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
#     serializer_class = APIUserModelSerializer
#     # queryset указывает, какие данные мы будем выводить в списке.
#     queryset = APIUser.objects.all()

#                   извлекать         выводит список   удаляет один объект
# class APIUserView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
class APIUserView(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet, CreateModelMixin):
    # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
    # моделью и будет работать с её данными.
    # serializer_class определяет тот Serializer, который мы будем использовать.
    # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # renderer_classes = [JSONRenderer]
    serializer_class = APIUserModelSerializer
    # queryset указывает, какие данные мы будем выводить в списке.
    queryset = APIUser.objects.all()

# class APIUserView(ViewSet):
#     # Использование произвольных команд
#     # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     # renderer_classes = [JSONRenderer]
#     @action(methods=['get'], detail=True)
#     def retrieve_name(self, request, pk=None):
#         user = get_object_or_404(APIUser, pk=pk)
#         # serializer = APIUserModelSerializer(user)
#         return Response({'first_name': user.first_name})
#
#     @action(methods=['get'], detail=False)
#     def list_all(self, request, pk=None):
#         # user = get_object_or_404(APIUser, many=True)
#         user = get_object_or_404(APIUser, many=True)
#         serializer = APIUserModelSerializer(user)
#         return Response(serializer.data)
#
#     def retreve(self, request, pk=None):
#         # serializer_class = APIUserModelSerializer
#         user = get_object_or_404(APIUser, pk=pk)
#         serializer = APIUserModelSerializer(user)
#         return Response(serializer.data)
