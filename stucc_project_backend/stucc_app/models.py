from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProfile(models.Model):
  bio = models.CharField(max_length=250)
  photo_path = models.ImageField(upload_to = 'profiles')
  career = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=CASCADE)


#resources
class Resource(models.Model):
  type = models.CharField(max_length=250)
  description = models.TextField()
  date_created = models.DateTimeField
  link = models.CharField(max_length=256)

#projects
class Project(models.Model):
  tag = models.CharField(max_length=256)
  title = models.CharField(max_length=256)
  description = models.TextField()
  photo_path = models.ImageField(upload_to = 'projects/')
  link = models.CharField(max_length=256)
  status = models.TextChoices('Status', 'OPEN ON_HOLD COMPLETE')
  date_created = models.DateTimeField()

#community
class Community(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  date_created = models.DateTimeField()
  creator = models.ForeignKey(UserProfile, on_delete=CASCADE)
  members = models.ManyToManyField(User)

#forums
class Forum(models.Model):
  name = models.CharField(max_length=140)
  description = models.TextField()
  cover_photo = models.ImageField(upload_to = 'forums/')
  date_created = models.DateTimeField()
  creator = models.ForeignKey(UserProfile, on_delete=CASCADE)
  members = models.ManyToManyField(User)

#posts
class Post(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField()
  photo_path = models.ImageField(upload_to = 'posts/')
  date_created = models.DateTimeField()
  poster = models.ForeignKey(UserProfile, on_delete=CASCADE)
  community = models.ForeignKey(Community, on_delete=CASCADE, default = 'general')
  forum = models.ForeignKey(Forum, on_delete=CASCADE, blank=True, null=True)

  #request
class Request(models.Model):
  tag = models.CharField(max_length=250)
  description = models.TextField()
  project = models.ForeignKey(Project, on_delete=CASCADE, default='general')

#responses
class Response(models.Model):
  description = models.TextField()
  request = models.ForeignKey(Request, on_delete=CASCADE)

