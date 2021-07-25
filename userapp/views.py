from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import APIUser
from .serializers import APIUserModelSerializer


# Create your views here.
namespace = 'userapp'

class APIUserModelViewSet(ModelViewSet):
    # Мы используем наследование от ModelViewSet. Это означает, что набор views связан с
    # моделью и будет работать с её данными.
    # serializer_class определяет тот Serializer, который мы будем использовать.
    # viewset определяет, какие данные будут вводиться, а serializer назначает их представление в JSON.
    serializer_class = APIUserModelSerializer
    # queryset указывает, какие данные мы будем выводить в списке.
    queryset = APIUser.objects.all()
