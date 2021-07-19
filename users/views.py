# from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


# Create your views here.


class UserModelViewSet(ModelViewSet):
    # [JSONRenderer] - выводит чистый JSON строку без HTML разметки
    # [BrowsableAPIRenderer] - выводит стилизацию в браузере для работы с JSON, можно включать и выключать настройку класса
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
    # моделью и будет работать с её данными.
    # serializer_class определяет тот Serializer, который мы будем использовать.
    # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
    serializer_class = UserModelSerializer
    # queryset указывает, какие данные мы будем выводить в списке.
    queryset = User.objects.all()

    # def get_renderers(self):
    #     """базовая настройка для класса BrowsableAPIRenderer"""
    #     pass