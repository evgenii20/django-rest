from rest_framework.serializers import HyperlinkedModelSerializer
# from .models import Author
from .models import APIUser


class APIUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        # сериализатор на основании модели User будет создавать JSON-представление
        # fields = '__all__'
        # при объявлении полей - быть внимательнее! иначе не грузится HTML-форма на странице
        # http://127.0.0.1:8000/api/userapp/
        # fields = ('user_name', 'first_name', 'last_name', 'email')
        fields = ('id', 'first_name', 'last_name', 'email')

