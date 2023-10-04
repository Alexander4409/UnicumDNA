from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    return render(request, 'DNAcon/home.html')


def signupuser(request):
    page = "register"
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower().strip()
            user.save()
            messages.success(request, "User account was created!")
            login(request, user)
            return redirect('current')
        else:
            messages.error(request, 'An error has occurred during registration!')

    context = {'page': page, 'form': form}
    return render(request, 'DNAcon/signupuser.html', context)




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

