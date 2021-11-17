from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, UserForm

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user(request):
    try:
        user = User.objects.all()
    except:
        user = None
    context = {
        'buyers': user,
    }
    return render(request, 'users/buyer_list.html',context)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
            form = UserForm()
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html',context)