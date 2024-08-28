from .serializer import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    serializer.data
    return Response(serializer.data)