from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
status = (
    ('New', 'New'),
    ('Accepted','Accepted'),
    ('Completed','Completed'),
    ('Cancelled','Cancelled'),
    )
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices = status, default='New')
    quantity = models.IntegerField()
    order_note = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.product.product_name + ' ordered by ' + self.user.username

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order)