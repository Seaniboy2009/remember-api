from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TasksList.as_view()),
]