from cgitb import Hook
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import LoginForm, UserForm, UserInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.views.generic import(View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
from .models import Contact, Hostel

def index(response):
     return render(response, 'main/index.html')

# Register and Login Page
def register_page(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)

            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            registered = True
        else:
            print(user_form.errors, user_info_form.errors)

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    return render(request, 'main/register.html', {'user_form':user_form, 'user_info_form':user_info_form, 'registered':registered})


def login_page(request):
    login_error = ''
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:  # login credentials matched
            if user.is_active:
                login(request, user)  # login successful
                return redirect(reverse('userapp:home'))
            else:
                return HttpResponse('Acount is not active')
        else:
            login_error = 'Invalid Login Details'

    return render(request, 'main/login.html', {'login_error': login_error, 'login_form': login_form})


@login_required
def home_page(request):
    return render(request, 'main/basic.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse('userapp:index'))

def contact(request):
    thank=False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(request)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'main/contact.html',{'thank':thank})  


def searchList(response):

    allHostels = []
    allHostels= Hostel.objects.values_list
    
    params = {'allHostels': allHostels}
    print(params)
    return render(response, 'main/searchList.html', params)   
    
