from django.shortcuts import render
from models import User
from rest_framework import viewsets
from rest_framework import permissions
from stucc_app.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  '''
  API endpoint that enables reading and editing of user data
  '''
  queryset = User.objects.all().order_by('-last_login')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
