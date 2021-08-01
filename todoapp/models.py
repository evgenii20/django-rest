from django.db import models
from django.utils import timezone

from userapp.models import APIUser


# Create your models here.
class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name='имя проекта')
    text = models.TextField(max_length=150, blank=True)
    users = models.ManyToManyField(APIUser)
    # users = models.OneToOneField(APIUser, on_delete=models.CASCADE)

    def __str__(self):
        """# __str__ применяется для отображения объекта в интерфейсе"""
        return f'Пользователь: {self.users} в проекте: {self.name}.'


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    todo = models.CharField(max_length=100)
    text = models.TextField(max_length=150, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    # users = models.OneToOneField(APIUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(APIUser)
    create_date = models.DateTimeField(auto_now_add=True)  # дата создания
    update_date = models.DateTimeField(auto_now_add=True)  # дата обновления

    class Meta:  # используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-create_date"]  # сортировка дел по времени их создания

    def __str__(self):
        return f'Заметка: {self.todo} от {self.create_date})'
