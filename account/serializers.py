from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

from account import models
from utils.common_utils import get_uuid


class LoginSerializer(serializers.ModelSerializer):
    """登陆注册Serializer"""
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
        user.open_id = get_uuid(length=20)
        user.save()
        return user


class MemberMiniSerializer(serializers.ModelSerializer):
    """成员MiniSerializer"""
    class Meta:
        model = models.Member
        read_only_fields = (
            'name',
            'id',
            'username',
            'avatar',
            'intro',
        )
        fields = read_only_fields + ()


class DepartmentMiniSerializer(serializers.ModelSerializer):
    """部门MixinSerializer"""
    manager = MemberMiniSerializer(read_only=True)
    class Meta:
        model = models.Department
        read_only_fields = (
            'name',
            'manager',
            'intro',
            'superior',
        )
        fields = read_only_fields + ()


class MemberSelfSerializer(serializers.ModelSerializer):
    """我的信息Serializer"""
    manager_departments = DepartmentMiniSerializer(many=True, read_only=True)
    class Meta:
        model = models.Member
        read_only_fields = (
            'id',
            'create_time',
            'open_id',
            'manager_departments',
            'departments',
        )
        fields = read_only_fields + (
            'username',
            'name',
            'gender',
            'avatar',
            'cellphone_no',
            'intro',
            'duty',
        )


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
            'name',
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


class DepartmentReadSerializer(serializers.ModelSerializer):
    """部门仅度Serializer"""
    manager = MemberMiniSerializer(read_only=True)
    members = MemberMiniSerializer(read_only=True, many=True)

    class Meta:
        model = models.Department
        read_only_fields = (
            'id',
            'create_time',
            'manager',
            'members',
            'name',
            'intro',
            'superior',
        )
        fields = read_only_fields + ()
