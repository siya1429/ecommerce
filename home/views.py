from django.shortcuts import render

# Create your views here.
def about(request):
  return render(request,'home/about.html')

def contact(request):
  return render(request,'home/contact.html')

def index(request):
  return render(request,'home/index.html')