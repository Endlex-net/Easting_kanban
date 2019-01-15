from rest_framework import serializers

from account import models
from utils import common_utils


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