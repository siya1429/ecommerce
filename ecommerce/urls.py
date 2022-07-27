from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    # path('home/',include('home.urls')),
    path('orders/',include('orders.urls')),
    path('products/',include('products.urls')),
    path('',include('home.urls')),
]
