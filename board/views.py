from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from board import models, serializers


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.filter()
    __doc__ = queryset.model._meta.verbose_name


class ProjectViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.filter()
    __doc__ = queryset.model._meta.verbose_name


