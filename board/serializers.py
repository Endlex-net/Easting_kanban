from rest_framework import serializers

from board import models
from utils import common_utils


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        read_only_fields = (
            'id',
            'create_time',
        )
        fields = read_only_fields + (
            'name',
            'members',
            'intro',
            'status',
            'source',
        )


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectManager
        read_only_fields = (
            'id',
            'create_time',
        )
        fields = read_only_fields + (
            'agent',
            'project',
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        read_only_fields = (
            'id',
            'create_time',
        )
        fields = read_only_fields + (
            'project',
            'status',
            'priority',
            'title',
            'manager',
            'workers',
            'todo_time',
            'start_time',
            'finish_time',
            'deadline',
        )
