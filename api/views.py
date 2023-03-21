from django.shortcuts import render

# Create your views here.
from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    

    
    