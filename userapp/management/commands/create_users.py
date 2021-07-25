# from django.contrib.auth.models import User

from userapp.models import APIUser
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')
        parser.add_argument('-p', '--prefix', type=str, help='Префикс для username')
        parser.add_argument('-a', '--admin', action='store_true', help='Создание учетной записи администратора')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                # User.objects.create_superuser(username=username, email='', password='123')
                APIUser.objects.create_superuser(username='gbdjango', email='', password='gbdjango')
                self.stdout.write(f'Суперпользователь {APIUser.username} создан успешно!')
            else:
                # User.objects.create_user(username=username, email='', password='123')
                APIUser.objects.create_user(username=username, email='', password='123')
