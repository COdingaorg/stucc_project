from django.shortcuts import render, redirect
from .models import User, UserProfile
from rest_framework import viewsets
from stucc_app.serializers import UserProfileSerializer, UserSerializer
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


#register User
def register_user(request):
  title = 'create account'
  form = RegisterUserForm
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      uname = form.cleaned_data['username']
      password = form.cleaned_data['password2']
      form.save()
      newlogin =  authenticate(request, username = uname, password = password)

      if newlogin:
        login(request, newlogin)

        messages.success(request, 'Account Created successfully. Add Profile')
        return redirect('user_profile')

      return redirect('login_user')
      
  context = {
    'form':form,
    'title':title
  }
  return render(request, 'django_registration/registration_form.html', context)

#login user
def login_user(request):
  title = 'Login to Your Account'
  form = LoginForm
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    newlogin =  authenticate(request, username = username, password = password)

    if newlogin is not None:
      login(request, newlogin)

      return redirect('/')
    else:
      messages.warning(request, 'Incorrect Username or Password')
  
  context = {
    'title':title,
    'form':form,
  }
  return render(request, 'registration/login.html', context)

#logout view function
@login_required(login_url='login')
def logout_user(request):
  '''
  logout a logged in user
  '''
  logout(request)

  return redirect('login_user')
#view function to user profile

@login_required(login_url='login')
def index(request):
  title = 'Welcome to StucC'

  context = {
    'title':title
  }

  return render(request, 'all_templates/indes.html', context)
  