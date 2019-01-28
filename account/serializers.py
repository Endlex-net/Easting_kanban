from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

from account import models
from django.contrib.auth import authenticate, login, logout
from utils import common_utils


class LoginSerializer(serializers.ModelSerializer):
    user_profile_model = models.Member

    class Meta:
        model = models.Member
        fields = (
            "username",
            "password",
        )

    def create(self, data):
        user = self.user_profile_model.objects.create(username=data['username'])
        user.set_password(data["password"])
        user.save()
        return user


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        read_only_fields = (
            'id',
            'create_time',
            'open_id',
        )
        fields = read_only_fields + (
            'username',
            'gender',
            'avatar',
            'cellphone_no',
            'intro',
            'duty',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        read_only_fields = (
            'id',
            'create_time',
        )
        fields = read_only_fields + (
            'name',
            'manager',
            'members',
            'intro',
            'superior',
        )