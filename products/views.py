from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def product_list(request):
  products = Product.objects.filter(is_active=True)
  return render(request,'products/product_list.html', { 'products': products })

def product_view(request, id):
  try:
    product = Product.objects.get(id=id, is_active=True)
    return render(request,'products/product_view.html', { 'product': product })
  except Product.DoesNotExist:
    return redirect('product_list') 
  
