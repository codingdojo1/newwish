from django.shortcuts import render, redirect
from django.contrib import messages, auth
import bcrypt
from .models import UserLogin
from .models import userManager
from django.contrib.auth.models import User

# Create your views here.
def new(req):
  return render(req, 'users/new.html')

def create(req):
  errors = userManager.validate_reg(req.POST)
  existing_users = UserLogin.objects.filter(email=req.POST['email'])
  if existing_users:
    errors.append("Email already in use")
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')

  pw_hash = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
  user =  UserLogin.objects.create(
    first_name=req.POST['first_name'],
    last_name=req.POST['last_name'],
    email=req.POST['email'],
    pw_hash=pw_hash,
  )
  req.session['user_id'] = user.id
  return redirect('wishes:index')

def login(req):
  errors = userManager.validate_login(req.POST)
  existing_users = UserLogin.objects.filter(email=req.POST['email'])
  if not existing_users:
    valid = False
    errors.append('Email or password invalid')
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')

  user = existing_users[0]
  if bcrypt.checkpw(req.POST['password'].encode(), user.pw_hash.encode()):
     valid = True
     result = user
  else:
    valid = False
    errors.append('Email or password invalid')

  if not valid:
    messages.error(req, result)
    return redirect('users:new')
  else:
    req.session['user_id'] = result.id
  return redirect('wishes:index')

def logout(req):
  req.session.clear()
  return redirect('users:new')
