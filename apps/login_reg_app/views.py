from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
  # request.session["errors"] = {}
  return render(request, "login_reg_app/index.html")

def register(request):
  check = User.objects.register(request.POST)
  request.session["reg_info"] = {
          "first_name": request.POST["first_name"],
          "last_name": request.POST["last_name"],
          "email": request.POST["email"].lower()
          }
  # print(check)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    request.session['fname'] = check['user'].first_name
    request.session['is_logged_in'] = True
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def fname(request):
  context = {"errors": "", "error_type": "fname"}
  error = User.objects.first_name(request.POST['first_name'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def lname(request):
  context = {"errors": "", "error_type": "lname"}
  error = User.objects.last_name(request.POST['last_name'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def email(request):
  context = {"errors": {}, "error_type": "email"}
  error = User.objects.email(request.POST['email'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def pword(request):
  context = {"errors": {}, "error_type": "pword"}
  error = User.objects.pword(request.POST['password'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def c_pword(request):
  context = {"errors": {}, "error_type": "c_pword"}
  error = User.objects.c_pword(request.POST['password_confirm'], request.POST['password'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def dob(request):
  context = {"errors": "", "error_type": "dob"}
  error = User.objects.dob(request.POST['dob'])
  context['errors'] = error
  return render(request, 'login_reg_app/partials/registration_partials.html', context)

def login(request):
  request.session["reg_info"] = {} #Once user is logged in stored reg details is cleared
  check = User.objects.login(request.POST)
  if check["is_valid"]:
    request.session["errors"] = {}
    request.session['uid'] = check['user'].id
    request.session['fname'] = check['user'].first_name
    request.session['is_logged_in'] = True
    return redirect('/welcome')
  else:
    request.session["errors"] = check["errors"]
    return redirect('/')

def logout(request):
  request.session.clear()
  request.session['is_logged_in'] = False
  return redirect('/')

