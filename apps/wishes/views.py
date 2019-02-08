import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Wish
from apps.users.models import UserLogin
# Create your views here.

def index(req):
    if 'user_id' not in req.session:
        return redirect('users:new')
    user = UserLogin.objects.get(id=req.session['user_id'])
    return render(req, 'wishes/index.html', {"wishes": Wish.objects.all(), "user": user})

context = {
    # 'wish_list': Wish.objects.exclude(creator=req.session['user_id']),
    # 'grant_list':,
}

def new(req):
    return render(req, 'wishes/new.html')

def grant(request):
    wish = Wish.objects.get(id=request.POST.get("wish_id"))
    wish.granted_at = datetime.datetime.now()
    wish.save()
    return redirect('wishes:index')

def create(request):
  # print(request.session['user_id'])
  user = UserLogin.objects.get(id=request.session['user_id'])

  data = {
    "name": request.POST.get("name", ""),
    "description": request.POST.get("description", ""),
    "creator": user
  }

  errors = []
  if not data['name']:
      errors.append("A wish must be at least three characters")
  if not data['description']:
      errors.append("Please provide a description.")
  if errors:
      return render(request, 'wishes/new.html', context={'errors': errors})

  wish = Wish.objects.create(
    name=request.POST.get("name"),
    description=request.POST.get("description"),
    creator=user
  )
  wish.save()
  from django.http import HttpResponse
  return redirect('wishes:index')
    #  return redirect('wishes:index')

# def create(req):
#   errors = UserLogin.objects.validate_reg(req.POST)
#   if errors:
#     for error in errors:
#       messages.error(req, error)
#     return redirect('wishes:new')
#   # create the product if there are no errors
#   Product.objects.create_product(req.POST, req.session['user_id'])
#   return redirect('wishes:index')

def edit(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    if request.method == "POST":
        errors = []
        if not request.POST.get("name"):
            errors.append("A wish must be at least three characters")
        if not request.POST.get("description"):
            errors.append("Please provide a description.")
        if errors:
            return render(request, 'wishes/edit.html', context={'errors': errors, 'wish': wish})

        wish.name = request.POST.get("name")
        wish.description = request.POST.get("description")
        wish.save()
        return redirect('wishes:index')
    else:
        return render(request, 'wishes/edit.html', context={'wish': wish})

def update(req):
    pass

def delete(req):
    wish = Wish.objects.get(id=req.POST.get("wish_id"))
    wish.delete()
    return redirect('wishes:index')
