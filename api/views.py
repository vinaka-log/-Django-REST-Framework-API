from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serialaizers import TaskSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objectsall()
    serializer_class = UserSerializer
    premission_classes =(AllowAny,)

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    serializer_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)