from rest_framework import generics, permissions
from .models import Task, TestingTask
from .serializers import TaskSerializer, TestingTaskSerializer
from rest_framework.views import APIView
from remember_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from remember_api.views import MyTokenObtainPairView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TasksList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()

    def perform_create(self, serializer):
        print('create')
        serializer.save(owner='admin')


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    queryset = Task.objects.all().order_by('-created_on')


# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
class TestingTaskListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = TestingTaskSerializer

    queryset = TestingTask.objects.all()