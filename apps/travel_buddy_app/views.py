from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages

def welcome(request):
  if request.session['is_logged_in']:
    all_trips  = Trip.objects.all()
    bookings = User.objects.get(id=request.session['uid']).bookings.all()
    other_bks = all_trips.difference(bookings)

    context = { 
      "bookings": bookings,
      "other_bks": other_bks
      }
    return render(request, "travel_buddy_app/welcome.html", context)
  return redirect(reverse('index'))
  
def logout(request):
  request.session['is_logged_in'] = False
  request.session.clear()
  return redirect(reverse('index'))

def add_trip(request):
  if request.session['is_logged_in']:
    return render(request, "travel_buddy_app/add_trip.html")
  return redirect(reverse('index'))

def add_trip_process(request):
  check = Trip.objects.add(request.POST, request.session['uid'])
  if type(check) == bool:
    return redirect('/welcome/add_trip')
  else:
    user_to_add_trip = User.objects.get(id=request.session['uid'])
    check.bookings.add(user_to_add_trip)
    return redirect("/welcome")

def info_trip(request, t_id):
  if request.session['is_logged_in']:
    # trip_to_view = Trip.objects.get(id=t_id)
    # other_bookings = trip_to_view.bookings.all()
    context = {
      "trip_info": Trip.objects.get(id=t_id),
      # "other_bookings": other_bookings.values()
    }
    return render(request, "travel_buddy_app/info_trip.html", context)
  return redirect(reverse('index'))

def join_trip(request, t_id):
  trip_to_add = Trip.objects.get(id=t_id)
  user_to_join = User.objects.get(id=request.session['uid'])
  trip_to_add.bookings.add(user_to_join)
  return redirect("/welcome")

# AJAX Functions
def dest(request):
  context = {"errors": "", "error_type": "dest"}
  error = Trip.objects.dest(request.POST['dest'])
  context['errors'] = error
  return render(request, 'travel_buddy_app/partials/add_trip_partials.html', context)

def desc(request):
  context = {"errors": "", "error_type": "desc"}
  error = Trip.objects.desc(request.POST['desc'])
  context['errors'] = error
  return render(request, 'travel_buddy_app/partials/add_trip_partials.html', context)

def start(request):
  context = {"errors": "", "error_type": "start"}
  error = Trip.objects.start(request.POST['start'])
  context['errors'] = error
  return render(request, 'travel_buddy_app/partials/add_trip_partials.html', context)

def end(request):
  context = {"errors": "", "error_type": "end"}
  error = Trip.objects.end(request.POST['end'], request.POST['start'])
  context['errors'] = error
  return render(request, 'travel_buddy_app/partials/add_trip_partials.html', context)