from django.urls import path
from .views import ProjectListCreateView,ProjectListView,TaskCreateView,TaskListView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path('create/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('list/', ProjectListView.as_view(), name='project-list'),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/list/", TaskListView.as_view(), name="tasks-list"),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),  # ✅ Update Task (Admin Only)
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),  # ✅ Delete Task (Admin Only)

]
