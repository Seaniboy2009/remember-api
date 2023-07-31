from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TasksList(generics.ListAPIView):

    # This gets the serialiser information to display 
    serializer_class = TaskSerializer

    # Query is set to all
    queryset = Task.objects.all()