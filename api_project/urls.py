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
from django.urls import path, include, re_path
# from rest_framework import permissions
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter, SimpleRouter
# from userapp.views import APIUserModelViewSet
from todoapp.views import ProjectModelViewSet, TodoModelViewSet

# Для автомтической генерации URL
from userapp.views import APIUserView
from todoapp.filters import ProjectListAPIView


from graphene_django.views import GraphQLView

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
# router.register('projects', ProjectModelViewSet, basename='projects')
# router.register('todo', TodoModelViewSet)
router.register('todo', TodoModelViewSet, basename='todo')

# "Access-Control-Allow-Origin:*"
# permission_classes - позволяет задать права на документацию
schema_view = get_schema_view(
    openapi.Info(
        title="Users",
        default_version='v1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
    # permission_classes - ожидает чтоб был кортеж List
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # получение токена
    path('api-token-auth/', obtain_auth_token),
    # path('api/filters/', include(router.urls))
    path('api/filters/kwargs/<str:name>/', ProjectListAPIView.as_view()),
    # path('api/users/<int:pk>/', APIUserRetrieveAPIView.as_view()),
    # path('api/users/<int:pk>/', APIUserDestroyAPIView.as_view()),

    # При использовании UrlPathVersioning мы можем передать номер версии в URL-адресе
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', APIUserView.as_view({'get': 'list'})),
    # re_path(r'^api/(?P<version>(v1|v2))/users/', APIUserView.as_view({'get': 'list'}))

    # NamespaceVersioning
    # path('api/v1/users/', include('userapp.urls', namespace='v1')),
    # path('api/v2/users/', include('userapp.urls', namespace='v2')),

    # drf-yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('swagger/', schema_view.with_ui('swagger'))
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('graphql/', GraphQLView.as_view(graphiql=True))

]
