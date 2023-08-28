from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from remember_api.permissions import IsOwnerOrReadOnly

class TasksList(generics.ListCreateAPIView):

    # This gets the serialiser information to display 
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Query is set to all
    queryset = Task.objects.all()

    # This is needed to assign an owner to the new task, or an error
    # will be thrown
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Task.objects.all().order_by('-created_on')