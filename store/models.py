from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):

    product_name = models.CharField(max_length=50,unique=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    create_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name