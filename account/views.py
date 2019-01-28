import datetime
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import list_route


from account import models, serializers


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
        return Response({'msg': 'create succeed', 'status': 'ok'})

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    def login(self, request):
        data = request.data
        member = authenticate(**data)
        if member:
            auth_login(request, member)
            return Response({'msg': 'Login succeed', 'status': 'ok'})
        else:
            return Response({'msg': 'Login failed', 'status': 'failed'})

    @action(detail=False, methods=['GET'])
    def logout(self, request):
        auth_logout(request)
        return Response({'msg': 'Logout', 'status': 'ok'})

class MemberViewSet(
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