from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Medium")  # ✅ Only one value allowed
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Pending")  # ✅ Only one value allowed
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title