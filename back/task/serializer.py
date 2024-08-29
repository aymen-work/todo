from rest_framework import serializers
from .models import Task
from datetime import datetime
from django.utils import timezone



class TaskSerializer(serializers.ModelSerializer):
    end_date = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
    def get_end_date(self, obj):
        if obj.end_date and obj.created_date:
            # Ensure obj.end_date is timezone-aware
            end_date = obj.end_date.astimezone(timezone.get_current_timezone())
            return end_date.strftime('%Y-%m-%d %I:%M %p')
        return None

    def get_created_date(self, obj):
        if obj.created_date:
            # Ensure obj.created_date is timezone-aware
            created_date = obj.created_date.astimezone(timezone.get_current_timezone())
            return created_date.strftime('%Y-%m-%d %I:%M %p')
        return None