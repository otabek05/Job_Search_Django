from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from . import forms
from main.models import Job
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('myprofile')
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('myprofile')
        else:
            return redirect('login')


    context={
        'title':'Profilga Kirish'
    }
    return render(
        request=request,
        template_name='user/login.html',
        context=context
    )

def user_logout(request):
    logout(request)
    return redirect('home')

def myprof(request):

    return render(request,'user/myprofile.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('myprofile')
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
            
    form = forms.UserRegisterForm()
    context ={
        'title': '',
        'form':form
    }
    return render(request=request, template_name='user/register.html', context=context)

def my_announce(request):
    sorts= Job.objects.filter(owner=request.user)
    

    context = {
        'sorts':sorts
    }

    return render(
        request=request,
        template_name='user/myprofile.html',
        context=context
    )
