from django.urls import path
from . import views

urlpatterns = [
  path('', views.welcome),
  path('logout/', views.logout), 
  path('add_trip/', views.add_trip),
  path('add_trip/add_trip_process/', views.add_trip_process),
  path('info_trip/<int:t_id>/', views.info_trip),
  path('join_trip/<int:t_id>/', views.join_trip),
  
  # AJAX Validation Paths
  path('add_trip/dest/', views.dest),
  path('add_trip/desc/', views.desc),
  path('add_trip/start/', views.start),
  path('add_trip/end/', views.end),
]