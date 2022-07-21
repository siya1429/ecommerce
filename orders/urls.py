from django.urls import path
from . import views

urlpatterns = [
    path('order_list/',views.order_list,name='order_list'),
    path('order_view/',views.order_view,name='order_view'),
]
