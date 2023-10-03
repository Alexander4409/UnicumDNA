from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

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


def currenttasks(reqest):
    return render(reqest, 'DNAcon/currenttasks.html')

