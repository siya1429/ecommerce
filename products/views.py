from django.shortcuts import render

# Create your views here.
def product_list(request):
  return render(request,'products/product_list.html')

def product_view(request):
  return render(request,'products/product_view.html')
  
