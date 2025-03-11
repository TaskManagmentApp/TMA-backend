from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Project,Task
from .serializers import ProjectSerializer,TaskSerializer

#create Project
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def create(self, request, *args, **kwargs):
        # Ensure only admin users can create projects
        if not request.user.is_staff:  # Assuming `is_staff` represents admin role
            return Response(
                {"error": "Permission denied: Only admins can create projects."},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().create(request, *args, **kwargs)

#list project
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access

#create Task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Only logged-in users can create tasks

    def create(self, request, *args, **kwargs):
        project_id = request.data.get("project")

        # ✅ Check if the project exists
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        return super().create(request, *args, **kwargs)
#list Task    
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Only authenticated users can view tasks

#update Task
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Only logged-in users can access

    def update(self, request, *args, **kwargs):
        # ✅ Check if the user is an admin
        if not request.user.is_staff:  
            return Response(
                {"error": "You do not have permission to update tasks."}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().update(request, *args, **kwargs)

#delete Task
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Only logged-in users can access

    def delete(self, request, *args, **kwargs):
        # ✅ Check if the user is an admin
        if not request.user.is_staff:
            return Response(
                {"error": "You do not have permission to delete tasks."}, 
                status=status.HTTP_403_FORBIDDEN
            )

        # ✅ Get the task
        task = self.get_object()
        task.delete()

        return Response(
            {"message": "Task deleted successfully."}, 
            status=status.HTTP_200_OK
        )
