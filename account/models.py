from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    address = models.TextField(max_length=500)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name+" | "+self.last_name

    def register(self):
        return self.save()


    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email=email)

        except:
            return False

    @staticmethod
    def get_customer_by_id(cusId):
        
        return Customer.objects.filter(id=cusId)


  