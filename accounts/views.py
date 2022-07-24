from django.shortcuts import render

# Create your views here.
def login(request):
  if request.method == 'POST':
    # print(request.POST)
    print('email:', request.POST['email'])
    print('password: ', request.POST['password'])
  return render(request,'accounts/login.html')

def profile(request):
  return render(request,'accounts/profile.html')

def register(request):
  return render(request,'accounts/register.html')
