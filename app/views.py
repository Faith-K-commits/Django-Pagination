from .serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets

class ProjectviewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()