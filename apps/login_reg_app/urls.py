from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register),
  path('login/', views.login),
  path('logout/', views.logout),
  # AJAX Validation Paths
  path('fname/', views.fname), #Ajax 
  path('lname/', views.lname), #Ajax
  path('email/', views.email), #Ajax 
  path('pword/', views.pword), #Ajax 
  path('c_pword/', views.c_pword), #Ajax 
  path('dob/', views.dob), #Ajax 

]