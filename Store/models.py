from account.models import Customer
from django.db import models
from account.models import Customer
import datetime
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def get_all_category():
        return Category.objects.all()


    def __str__(self):
            return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'uploads/products' )


    def __str__(self):
        return self.name 


    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_all_products_by_id(categoryID):

        if categoryID:

            return Product.objects.filter(category=categoryID)
        else:
            return Product.get_all_products()

    # @staticmethod
    # def get_product_by_id(ids):
    #     return Product.objects.filter(id=ids)


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1,null=True)
    price = models.IntegerField()
    address = models.CharField(max_length=100,blank=True,default='')
    phone = models.CharField(max_length=14,blank=True,default='')
    date = models.DateField(default=datetime.datetime.today)
    time = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    present = models.BooleanField(default=False)
    
    @staticmethod
    def get_order_by_customer_id(cus_id):
            return Order.objects.filter(customer=cus_id).order_by('-time')
    