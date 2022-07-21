from django.shortcuts import render

# Create your views here.
def order_list(request):
  return render(request,'orders/order_list.html')

def order_view(request):
  return render(request,'orders/order_view.html')