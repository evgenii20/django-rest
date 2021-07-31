from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from .models import Project, Todo
from .serializers import ProjectModelSerializer


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ('name',)


class TodoFilter(filters.FilterSet):
    project = filters.CharFilter(lookup_expr='contains')
    # create_date = filters.DateTimeFilter()

    class Meta:
        model = Todo
        # fields = ('project', 'create_date')
        fields = ('project',)


# class ProjectListView(ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer
#     filter_backends = [filters.SearchFilter]

# from rest_framework import filters
#


# class ProjectListAPIView(ListAPIView):
# class ProjectListAPIView(GenericAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer
#     # filter_backends = [filters.SearchFilter]
#     search_fields = ['name']

# def list(self, request):
#     queryset = self.Project.objects.all()
#     serializer = ProjectModelSerializer(self.get_queryset(), many=True)
#     return Response(serializer.data)

# def get_queryset(self):
#     name = self.request.query_params.getlist('name', None)
#     # queryset = self.Project.objects.all()
#     if name:
#         # Projects_name = Projects_name.filter(name__contains=name)
#         return self.queryset.filter(name__contains=name)
#     return self.queryset

# class ProjectListAPIView(ListAPIView):
#     serializer_class = ProjectModelSerializer
#     # queryset = Project.objects.all()
#
#     # @action(methods=['get'], detail=False)
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         queryset = Project.objects.all()
#         name = self.request.query_params.get('name')
#         if name is not None:
#             queryset = queryset.filter(project__name=name)
#         return queryset

class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectModelSerializer
    # serializer_class = ProjectFilter
    filter_backends = [SearchFilter]
    # http://example.com/api/users?search=russell

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name=name)
