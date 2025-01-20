from django.db import models
from . import views
# Create your models here.
# Model for Contact Page
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    desc=models.TextField(max_length=1000)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.name
    
#model for Product Page
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product_name


 