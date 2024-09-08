from .serializer import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from datetime import datetime

@api_view(['GET'])
def get_tasks(request,status=None):
    tasks = Task.objects.all().filter(status=status) if status != None else Task.objects.all() 
    serializer = TaskSerializer(tasks,many=True).data
    for s in serializer:
        s['end_date'] = datetime.strptime(s['end_date'], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %I:%M %p")
    return Response(serializer)

class GetUpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # def create(self, request, *args, **kwargs):
    #     # Print the incoming data
    #     print("Received data:__⚠️⚠️⚠️__", request.data)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)