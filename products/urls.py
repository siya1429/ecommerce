from django.urls import path
from . import views

urlpatterns = [
    path('product_list/',views.product_list,name='product_list'),
    path('product_view/',views.product_view,name='product_view'),
]
