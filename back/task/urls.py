from django.urls import path
from . import views,api

urlpatterns = [
    path('v1/tasks',api.get_tasks,name='get_tasks'),
<<<<<<< HEAD
    path('v1/tasks/<str:status>',api.get_tasks,name='get_tasks'),
=======
>>>>>>> parent of debec4f (feature: add filtering tasks in home page)
    path('v2/tasks/<int:id>',api.GetUpdateTask.as_view(),name='GetUpdateTask'),
    path('v2/addtask',api.CreateTask.as_view(),name='CreateTask'),
]