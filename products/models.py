from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=150)
  description = models.TextField(blank=True, null=True)
  stock = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  is_active = models.BooleanField(default=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name