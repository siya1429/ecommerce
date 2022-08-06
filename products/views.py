from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.
def product_list(request):
  category = request.GET.get('category', None)

  products = Product.objects.filter(is_active=True)
  if category:
    products = products.filter(category__name=category)

  categories = Category.objects.all()
  return render(request,'products/product_list.html', { 'products': products, 'categories': categories })

def product_view(request, id):
  try:
    product = Product.objects.get(id=id, is_active=True)
    return render(request,'products/product_view.html', { 'product': product })
  except Product.DoesNotExist:
    return redirect('product_list')
  
