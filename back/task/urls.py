from django.urls import path
from . import views,api

urlpatterns = [
    path('v1/tasks',api.get_tasks,name='get_tasks'),
]