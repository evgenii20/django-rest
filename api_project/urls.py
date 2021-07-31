"""api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
# from userapp.views import APIUserModelViewSet
from todoapp.views import ProjectModelViewSet, TodoModelViewSet

# Для автомтической генерации URL
from userapp.views import APIUserView
from todoapp.filters import ProjectListAPIView

# from todoapp.views import ProjectCustomFilterViewSet

router = DefaultRouter()
# router = SimpleRouter()

# Добавляем точку входа
router.register('users', APIUserView, basename='users')
# router.register('users', APIUserModelViewSet)
router.register('projects', ProjectModelViewSet, basename='projects')
# поиск по параметрам
# router.register('param', ArticleParamFilterViewSet)
# router.register('filters', ProjectModelViewSet, basename='filters')
# router.register('projects', ProjectModelViewSet.as_view(), basename='projects')
# router.register('todo', TodoModelViewSet)
router.register('todo', TodoModelViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/filters/', include(router.urls))
    path('api/filters/kwargs/<str:name>/', ProjectListAPIView.as_view())
    # path('api/users/<int:pk>/', APIUserRetrieveAPIView.as_view()),
    # path('api/users/<int:pk>/', APIUserDestroyAPIView.as_view()),

]
