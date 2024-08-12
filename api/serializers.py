from rest_framework import serializers
from tasks.models import Task, TelegramUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'created_by', 'assigned_to']
        read_only_fields = ['created_by']

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id', 'user', 'telegram_id']