from rest_framework.pagination import PageNumberPagination
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        projects = Project.objects.all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_projects = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(paginated_projects, many=True)
        return paginator.get_paginated_response(serializer.data)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)