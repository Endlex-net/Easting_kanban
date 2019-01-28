import datetime
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from account import models, serializers
from utils.mixins import RbacMemberMixin


class AuthViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin):
    permission_classes = ()
    serializer_class = serializers.LoginSerializer
    profile_serializer_class = serializers.LoginSerializer
    queryset = models.Member.objects.filter()

    __doc__ = "auth"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    def login(self, request):
        data = request.data
        member = authenticate(**data)
        if member:
            auth_login(request, member)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['GET'])
    def logout(self, request):
        auth_logout(request)
        return Response(status=status.HTTP_200_OK)


class MemberViewSet(
    RbacMemberMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.filter()
    __doc__ = queryset.model._meta.verbose_name

    @action(detail=False, methods=["GET"])
    def myself(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class DepartmentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.DepartmentSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action in ['retrieve', 'list']:
            return serializers.DepartmentReadSerializer
        else:
            return self.serializer_class
    queryset = models.Department.objects.filter()
    __doc__ = queryset.model._meta.verbose_name