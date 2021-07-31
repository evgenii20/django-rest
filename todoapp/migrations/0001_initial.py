# Generated by Django 3.2.5 on 2021-07-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('text', models.TextField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('todo', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
