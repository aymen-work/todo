from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):
    end_date = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
    def get_end_date(self, obj):
        if obj.end_date:
            return obj.end_date.strftime('%Y-%m-%d %I:%M %p')  # Format as 'YYYY-MM-DD'
        return None