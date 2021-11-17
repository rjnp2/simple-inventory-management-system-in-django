from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from store.models import Product
from order.models import Delivery, Order
from django.contrib.auth.models import User
from order.forms import OrderForm
from django.contrib import messages

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    try:
        total_delivery = Delivery.objects.count()
    except:
        total_delivery = 0
    total_order = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    total_user = User.objects.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            product_name = form.cleaned_data.get('product')
            quantity = form.cleaned_data.get('quantity')
            current_user = request.user

            is_order_exist = Order.objects.filter(product=product_name,user=current_user).exists()
            if is_order_exist:
                order = Order.objects.get(product=product_name,user=current_user)
                order.quantity += quantity
                order.save()

            else:
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
            
            messages.success(request, f'{product_name} has been order')
            return redirect('dashboard')
    else:
        form = OrderForm()

    context = {
        'form': form,
        'product': total_product,
        'delivery': total_delivery,
        'order': total_order,
        'orders': orders,
        'total_user':total_user
    }
    return render(request, 'dashboard.html',context)