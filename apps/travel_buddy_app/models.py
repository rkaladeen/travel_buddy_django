from django.db import models
from datetime import datetime, date
from ..login_reg_app.models import *

class TripManager(models.Manager):
  def add(self, postData, uid):
    is_valid = True
    if len(postData['dest']) < 5:
      is_valid = False
    elif len(postData['dest']) < 10:
      is_valid = False
    elif len(postData['start']) < 1:
      is_valid = False
    else:
      start = datetime.strptime(postData, "%Y-%m-%d")
      if start < datetime.now():
        is_valid = False
    if len(postData['end']) < 1:
      is_valid = False
    else:
      start = datetime.strptime(postData['start'], "%Y-%m-%d")
      end = datetime.strptime(postData['end'], "%Y-%m-%d")
      if end < start:
        is_valid = False       
    if is_valid:
      return Trip.objects.create(
        user_id = uid,
        destination = postData['dest'],
        desc = postData['desc'],
        start = postData['start'],
        end = postData['end']
      )
    else:
      return is_valid
  
  def dest(self, postData):
    error = ""
    if len(postData) < 1:
      error = "Destination is required!"
    elif len(postData) < 5:
      error = "Destination must be 5 character or longer!"
    return error 

  def desc(self, postData):
    error = ""
    if len(postData) < 1:
      error = "Description is required!"
    elif len(postData) < 10:
      error = "Description must be 10 character or longer!"
    return error 

  def start(self, postData):
    error = ""
    if len(postData) < 1:
      error = "Start Date is required!"
    else:
      start = datetime.strptime(postData, "%Y-%m-%d")
      if start < datetime.now():
        error = "Start Date must be in the future"       
      # else:
      #   today = date.today() 
      #   lead_time = start.day + today.day - ((today.year, today.month) > (start.year, start.month)) 
      #   print(lead_time)
      #   if lead_time < 15:
      #     error = "You must plan a trip 14 days in advance" 
    return error

  def end(self, postData1, postData2):
    error = ""
    if len(postData1) < 1:
      error = "End Date is required!"
    else:
      start = datetime.strptime(postData2, "%Y-%m-%d")
      end = datetime.strptime(postData1, "%Y-%m-%d")
      if end < start:
        error = "End date must be after start date"       
    return error

class Trip(models.Model):
  # id auto-generated
  user = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
  destination = models.CharField(max_length=45)
  desc = models.TextField()
  start = models.DateField(null=True)
  end = models.DateField(null=True)
  bookings = models.ManyToManyField(User, related_name="bookings")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TripManager()
  

