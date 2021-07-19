from rest_framework.serializers import HyperlinkedModelSerializer
# from .models import Author
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        # сериализатор на основании модели User будет создавать JSON-представление
        fields = '__all__'
