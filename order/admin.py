from django.contrib import admin
from .models import Order, Delivery

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity','user','status', 'order_note','created_at']

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'courier_name','created_date']

admin.site.register(Order,OrderAdmin)
admin.site.register(Delivery,DeliveryAdmin) 
    