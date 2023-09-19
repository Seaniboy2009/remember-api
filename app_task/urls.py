from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TasksList.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('testingtasks/', views.TestingTaskListView.as_view()),
]