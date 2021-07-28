from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, UserProfile
from django import forms

class RegisterUserForm(UserCreationForm):
  class Meta:
    model = User
    
    widgets = {
      'username':forms.TextInput(attrs={'placeholder':'Username','class':'profile_input'}),
      'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'profile_input'}),
      'last_name':forms.TextInput(attrs={'placeholder':'Last Name','class':'profile_input'}),
      'password1':forms.PasswordInput(attrs={'placeholder':'Password','class':'profile_input'}),
      'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'profile_input'}),
    }
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['__all__']

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    
    widgets = {
      'bio':forms.TextInput(attrs={'placeholder':'Bio...','class':'bio_input'}),
      'photo_path':forms.Textarea(attrs={'placeholder':'Add Photo','class':'photo_input'}),
      'career':forms.TextInput(attrs={'placeholder':'Career'}),
    }
    fields = ('bio','photo_path', 'career' )


