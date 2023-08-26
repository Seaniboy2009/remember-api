from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from remember_api.permissions import IsOwnerOrReadOnly

class TasksList(generics.ListAPIView):

    # This gets the serialiser information to display 
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Query is set to all
    queryset = Task.objects.all()