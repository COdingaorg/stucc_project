from rest_framework import serializers
from django.contrib.auth.models import UserManager

class UserSerializer(serializers.Serializer):
  '''
  user model serializer, model has been imported from django auth models
  '''
  id = serializers.IntegerField(read_only = True)
  username = serializers.CharField(required = True, max_lenght = 30)
  first_name = serializers.CharField(required = True, max_lenght = 15)
  last_name = serializers.CharField(required = True, max_length = 20)
  email = serializers.EmailField()
  password = serializers.CharField(
    write_only=True,
    required=True,
    help_text='Leave empty if no change needed',
    style={'input_type': 'password', 'placeholder': 'Password'}
    )
  last_login = serializers.DateTimeField()
  date_joined = serializers.DateTimeField()
  is_superuser = serializers.BooleanField()
  is_staff = serializers.BooleanField()
  is_active = serializers.BooleanField()
  

