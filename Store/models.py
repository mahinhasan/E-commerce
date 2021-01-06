from django.db import models

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



    @staticmethod
    def get_all_products():
        return Product.objects.all()