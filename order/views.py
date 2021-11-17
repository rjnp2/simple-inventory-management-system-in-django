from django.shortcuts import render,redirect
from .models import Order, Delivery
from django.contrib.auth.decorators import login_required
from .forms import DeliveryForm
from django.contrib import messages
from store.models import Product

# Create your views here.
@login_required(login_url='login')
def order(request):
    order = Order.objects.all().order_by('-id')
    context = {
        'orders': order,
    }
    return render(request, 'order/order_list.html',context)

@login_required(login_url='login')
def delivery(request):
    try:
        total_delivery = Delivery.objects.all()
    except:
        total_delivery = None

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            instance = form.save()
            order = Order.objects.get(id=instance.order.id)
            product = Product.objects.get(product_name=order.product.product_name)
            product.stock -= order.quantity
            product.save()

            order.status = 'completed'
            order.save()
            product_name = form.cleaned_data.get('order.product_name')
            messages.success(request, f'{product_name} has been delivery')
            
            return redirect('dashboard')
    else:
        form = DeliveryForm()

    context = {
        'delivery': total_delivery,
        'form':form
    }
    return render(request, 'order/delivery_list.html',context)
