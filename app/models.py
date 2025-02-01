from django.db import models
from uuid import uuid4

class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title