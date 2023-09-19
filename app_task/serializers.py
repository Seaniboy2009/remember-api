from rest_framework import serializers
from .models import Task, TestingTask


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer for the task model """

    # Changes the onwer id number to the username 
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = '__all__'

class TestingTaskSerializer(serializers.ModelSerializer):
    """ Serializer for the task model """

    # Changes the onwer id number to the username 
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TestingTask
        fields = '__all__'