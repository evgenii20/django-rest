import graphene
from graphene_django import DjangoObjectType

from todoapp.models import Project, Todo
from userapp.models import APIUser


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class APIUserType(DjangoObjectType):
    class Meta:
        model = APIUser
        fields = '__all__'


# Тест
# # class Query(graphene.ObjectType):
# #     hello = graphene.String(default_value="Hi!")

# Запросы на чтение данных
class Query(graphene.ObjectType):
    all_APIUser = graphene.List(APIUserType)

    # def resolve_all_apiuser(root, info):
    def resolve_all_APIUser(self, info):
        return APIUser.objects.all()

    all_Todo = graphene.List(TodoType)

    def resolve_all_Todo(root, info):
        return Todo.objects.all()

    # запросы с параметрами для одного запроса
    user_by_id = graphene.Field(APIUserType, id=graphene.Int(required=True))

    def resolve_user_by_id(self, info, id):
        # создаём функцию resolve
        try:
            return APIUser.objects.get(id=id)
        except APIUser.DoesNotExist:
            return None

    # запросы с параметрами для нескольких запроса
    #     Фильтрация данных
    # необязательный(False) параметр (required=False)
    project_by_user = graphene.List(ProjectType, name=graphene.String(required=False))

    # можем передавать более 1-го параметра:
    # project_by_user = graphene.List(ProjectType, name=graphene.String(required=False), id=graphene.Int(required=True))

    def resolve_project_by_user(self, info, name=None):
        # создаём функцию resolve
        projects = Project.objects.all()
        # if last_name:
        if name:
            projects = projects.filter(name=name)
        return projects


# Изменение данных. Мутации
class APIUserUpdateMutation(graphene.Mutation):
    class Arguments:
        # параметры мутации
        id = graphene.ID()
        # email = graphene.Int(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(APIUserType)

    @classmethod
    def mutate(cls, root, info, email, id):
        # мутация модели APIUser
        user = APIUser.objects.get(pk=id)
        user.email = email
        user.save()
        return APIUserUpdateMutation(user=user)

class APIUserCreateMutation(graphene.Mutation):
    class Arguments:
        # параметры мутации
        first_name = graphene.String()
        last_name = graphene.String()
        # email = graphene.Int(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(APIUserType)

    # создаём объект из переданных параметров
    @classmethod
    def mutate(cls, root, info, first_name, last_name, email):
        # мутация модели APIUser
        user = APIUser(first_name=first_name, last_name=last_name, email=email)
        # user.email = email
        user.save()
        return APIUserCreateMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = APIUserUpdateMutation.Field()
    create_user = APIUserCreateMutation.Field()


# schema = graphene.Schema(query=Query)
# с мутациями:
schema = graphene.Schema(query=Query, mutation=Mutation)
