from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def product(request):
    product = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('product_name')
            messages.success(request, f'{product_name} has been added')
            return redirect('product')
    else:
        form = ProductForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'store/product_list.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['Admin'])
def product_delete(request, id):
    item = Product.objects.get(id=id)
    item.delete()
    return redirect('product')