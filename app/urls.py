from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectviewSet
app_name = 'app'

router = DefaultRouter()
router.register(r'projects', ProjectviewSet)
urlpatterns = [
   path('', include(router.urls)),
]