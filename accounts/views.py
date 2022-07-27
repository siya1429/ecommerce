from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('index')

  return render(request,'accounts/login.html')

@login_required()
def profile(request):
  user = request.user
  return render(request,'accounts/profile.html', { 'user': user })

def register(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User(email=email, username=username)
    user.set_password(password)
    user.save()

    return redirect('index')

  return render(request,'accounts/register.html')


def logout_view(request):
  logout(request)
  return redirect('index')
