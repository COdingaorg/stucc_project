from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.login_user, name = 'login'),
  url(r'home', views.index, name= 'home'),
  url(r'^register_user/$', views.register_user, name = 'register_user'),
  url(r'^login_user/$', views.login_user, name = 'login_user'),
  url(r'^logout_user/$', views.logout_user, name = 'logout_user'),
  url(r'^profile/$', views.add_user_profile, name = 'user_profile'),

]