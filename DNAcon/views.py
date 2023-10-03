from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'DNAcon/home.html')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'DNAcon/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request,user)
                return redirect('current')

            except IntegrityError:

                return render(request, 'DNAcon/signupuser.html',
                      {'form': UserCreationForm(),
                       'error':'Пользователь с таким именем уже существует!'})

        else:
            return render(request, 'DNAcon/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпадают!'})


def loginuser(request):
    if request.method == "GET":
        return render(request,'DNAcon/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'DNAcon/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа!'})
        else:
            login(request,user)
            return redirect('current')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def currenttasks(reqest):
    return render(reqest, 'DNAcon/currenttasks.html')

