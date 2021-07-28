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
  return render(request, 'register_login.html', context)

#login user
def login_user(request):
  title = 'Login to Your Account'
  form = LoginForm
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    newlogin =  authenticate(request, username = username, password = password)
    if newlogin:
      login(request, newlogin)

      messages.success(request, 'Login successful. Add Profile to proceed')
      return redirect('user_profile')

    else:
      messages.warning(request, 'Incorrect Username or Password')
      return redirect('login_user')
  
  
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

  return render(request, 'all_templates/index.html', context)

@login_required(login_url='login')
def add_user_profile(request):
  title = f'{request.user.username}'

  context = {
    'title':title
  }

  return render(request, 'all_templates/profile.html', context)
  
# view function to community page
@login_required(login_url='login')
def community(request):
  '''
  renders community page
  '''
  title = 'join a community'

  context = {
    'title':title
  }
  return render(request, 'all_templates/community.html', context)

#view function for forums page
@login_required(login_url='login')
def forums(request):
  '''
  renders forum page
  '''
  title = 'join a forum'

  context = {
    'title':title
  }
  return render(request, 'all_templates/forums.html', context)

# view function rendering projects page
@login_required(login_url='login')
def projects(request):
  '''
  renders projects page
  '''
  title = 'Open projects - Create yours'

  context = {
    'title':title
  }
  return render(request, 'all_templates/projects.html', context)