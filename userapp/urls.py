# NamespaceVersioning
from django.urls import path
from .views import APIUserView

app_name = 'userapp'
urlpatterns = [
    # path('', APIUserView.as_view()),
    # все вьюсеты конструируем в ручную
    path('', APIUserView.as_view({'get': 'list'})),
    # path('<id>', APIUserView.as_view({'get': 'list'})),
]