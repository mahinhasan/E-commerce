from django.contrib import admin

# Register your models here.
from .models import *

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order,AdminOrder)
