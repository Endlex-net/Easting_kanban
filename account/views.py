from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from account import models, serializers


class MemberViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.filter()
    __doc__ = queryset.model._meta.verbose_name


class DepartmentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializers_class = serializers.MemberSerializer
    queryset = models.Department.objects.filter()
    __doc__ = queryset.model._meta.verbose_name