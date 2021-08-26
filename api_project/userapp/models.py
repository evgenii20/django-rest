from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class APIUser(AbstractUser):
    # id = models.BigAutoField(primary_key=True)
    # user_name = models.CharField(max_length=64, verbose_name='имя пользователя')
    # first_name = models.CharField(max_length=64, verbose_name='имя')
    # last_name = models.CharField(max_length=64, verbose_name='фамилия')
    # birthday_year = models.PositiveIntegerField()
    # age = models.PositiveSmallIntegerField(verbose_name='возраст', blank=True)
    email = models.EmailField(verbose_name='email', unique=True)
    # password = models.CharField(max_length=50)

# class UserProfile(models.Model):
# id = models.BigAutoField(primary_key=True)
# username = models.CharField(max_length=64, verbose_name='имя пользователя')
# first_name = models.CharField(max_length=64, verbose_name='имя')
# last_name = models.CharField(max_length=64, verbose_name='фамилия')
# birthday_year = models.PositiveIntegerField()
# age = models.PositiveSmallIntegerField(verbose_name='возраст', blank=True)
# email = models.EmailField(verbose_name='email', unique=True)
# password = models.CharField(max_length=50)

