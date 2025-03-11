from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('standard', 'Standard User'),
]

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('standard', 'Standard User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='standard')
    phone = models.CharField(max_length=15, null=True, blank=True)  # ✅ Add phone field
    address = models.TextField(null=True, blank=True)  # ✅ Add address


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
