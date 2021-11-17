from django import forms

from .models import Order, Delivery

status = (
    ('New', 'New'),
    ('Accepted','Accepted'),
    )
class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['order','courier_name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['product', 'quantity', 'order_note']