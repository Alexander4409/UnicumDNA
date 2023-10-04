from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from .models import UserProfile
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

            # Проверяем, существует ли профиль пользователя, и создаем его, если нет
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.save()

            # Получаем выбранную группу из формы и добавляем пользователя в неё
            group = form.cleaned_data['group']

            # Пример: добавление пользователя в группу "ИП-64"
            if group == 'ИП-64':
                user.groups.add(Group.objects.get(name='ИП-64'))
            # Пример: добавление пользователя в группу "ИП-65"
            elif group == 'ИП-65':
                user.groups.add(Group.objects.get(name='ИП-65'))
            # Добавьте другие группы по аналогии

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


from django.shortcuts import render
from .models import StudyMaterial
def currenttasks(reqest):
    materials = StudyMaterial.objects.all()
    return render(reqest, 'DNAcon/currenttasks.html', {'materials': materials})

