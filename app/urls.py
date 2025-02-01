from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('projects/', views.project, name='projects'),
]