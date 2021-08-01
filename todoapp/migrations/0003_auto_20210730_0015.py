# Generated by Django 3.2.5 on 2021-07-29 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='имя проекта'),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='users',
        ),
        migrations.AddField(
            model_name='todo',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
