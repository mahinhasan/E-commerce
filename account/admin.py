from django.contrib import admin
from django.contrib.admin.decorators import register
from . models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone']


admin.site.register(Customer,CustomerAdmin)