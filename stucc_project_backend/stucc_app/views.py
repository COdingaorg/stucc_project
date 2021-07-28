from django.shortcuts import render
from .models import User, UserProfile
from rest_framework import viewsets
from rest_framework import permissions
from stucc_app.serializers import UserProfileSerializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  '''
  API endpoint that enables reading and editing of user data
  '''
  queryset = User.objects.all().order_by('-last_login')
  serializer_class = UserSerializer
  
  # permission_classes = [permissions.IsAuthenticated]

#user profile viewset
class UserProfileViewSet(viewsets.ModelViewSet):
  '''
  API endpoint that enables reading and editing of user data
  '''
  queryset = UserProfile.objects.all().order_by('-id')
  serializer_class = UserProfileSerializer
  

