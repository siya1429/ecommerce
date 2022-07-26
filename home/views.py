from ctypes import cdll
from django.shortcuts import render, redirect
from .models import Contact
from django import forms

class ContactForm(forms.Form):
  email = forms.CharField(required=False)
  full_name = forms.CharField()
  phone = forms.CharField()
  messsage = forms.TextInput()

# Create your views here.
def about(request):
  return render(request,'home/about.html')

def contact(request):
  if request.method == 'POST':
    print(request.POST)
    c = ContactForm(request.POST)

    if c.is_valid():
      print(c.cleaned_data)

      # Method 1
      # Contact.objects.create(email=data['email'], phone=data['phone'], message=data['message'], full_name=data['full_name'])

      # Method 2
      c = Contact(**c.cleaned_data)
      c.save()
      return redirect('index')
    else:
      pass
  return render(request,'home/contact.html')

def index(request):
  return render(request,'home/index.html')