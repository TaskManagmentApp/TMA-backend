from rest_framework import serializers
from .models import Project,Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # Or specify fields like ['id', 'name', 'description']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"  # Ensure 'project' is included

    def validate_project(self, value):
        """Ensure the project exists before assigning it to the task."""
        if not Project.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Project does not exist.")
        return value