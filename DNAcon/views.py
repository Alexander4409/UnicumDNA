from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, UserFileForm
from .models import UserProfile, StudyMaterial,UserFile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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
            # elif group == 'ИП-51':
            #     user.groups.add(Group.objects.get(name='ИП-51'))
            # elif group == 'ИП-50':
            #     user.groups.add(Group.objects.get(name='ИП-50'))
            # elif group == 'ИП-52':
            #     user.groups.add(Group.objects.get(name='ИП-52'))
            # elif group == 'ИП-53':
            #     user.groups.add(Group.objects.get(name='ИП-53'))
            # elif group == 'ИП-54':
            #     user.groups.add(Group.objects.get(name='ИП-54'))
            # elif group == 'ИП-55':
            #     user.groups.add(Group.objects.get(name='ИП-55'))
            # elif group == 'ИП-61':
            #     user.groups.add(Group.objects.get(name='ИП-61'))
            # elif group == 'ИП-62':
            #     user.groups.add(Group.objects.get(name='ИП-62'))
            # elif group == 'ИП-63':
            #     user.groups.add(Group.objects.get(name='ИП-63'))
            # elif group == 'ИЭ-71':
            #     user.groups.add(Group.objects.get(name='ИЭ-71'))
            # elif group == 'ИЭ-72':
            #     user.groups.add(Group.objects.get(name='ИЭ-72'))
            # elif group == 'ИЭ-81':
            #     user.groups.add(Group.objects.get(name='ИЭ-81'))
            # elif group == 'ИЭ-82':
            #     user.groups.add(Group.objects.get(name='ИЭ-82'))
            # elif group == 'ИЭ-9':
            #     user.groups.add(Group.objects.get(name='ИЭ-9'))
            # elif group == 'ИЭ-10':
            #     user.groups.add(Group.objects.get(name='ИЭ-10'))
            # elif group == 'ИЭ-11':
            #     user.groups.add(Group.objects.get(name='ИЭ-11'))
            # elif group == 'Р-71':
            #     user.groups.add(Group.objects.get(name='Р-71'))
            # elif group == 'Р-72':
            #     user.groups.add(Group.objects.get(name='Р-72'))
            # elif group == 'Р-81':
            #     user.groups.add(Group.objects.get(name='Р-81'))
            # elif group == 'Р-82':
            #     user.groups.add(Group.objects.get(name='Р-82'))
            # elif group == 'Р-9':
            #     user.groups.add(Group.objects.get(name='Р-9'))
            # elif group == 'Р-10':
            #     user.groups.add(Group.objects.get(name='Р-10'))
            # elif group == 'ИИ-71':
            #     user.groups.add(Group.objects.get(name='ИИ-71'))
            # elif group == 'ИИ-72':
            #     user.groups.add(Group.objects.get(name='ИИ-72'))
            # elif group == 'ИИ-81':
            #     user.groups.add(Group.objects.get(name='ИИ-81'))
            # elif group == 'ИИ-82':
            #     user.groups.add(Group.objects.get(name='ИИ-82'))
            # elif group == 'ИИ-9':
            #     user.groups.add(Group.objects.get(name='ИИ-9'))
            # elif group == 'ИИ-10':
            #     user.groups.add(Group.objects.get(name='ИИ-10'))
            # elif group == 'ИИ-11':
            #     user.groups.add(Group.objects.get(name='ИИ-11'))
            # elif group == 'П-51':
            #     user.groups.add(Group.objects.get(name='П-51'))
            # elif group == 'П-52':
            #     user.groups.add(Group.objects.get(name='П-52'))
            # elif group == 'П-53':
            #     user.groups.add(Group.objects.get(name='П-53'))
            # elif group == 'П-54':
            #     user.groups.add(Group.objects.get(name='П-54'))
            # elif group == 'П-55':
            #     user.groups.add(Group.objects.get(name='П-55'))
            # elif group == 'П-61':
            #     user.groups.add(Group.objects.get(name='П-61'))
            # elif group == 'П-62':
            #     user.groups.add(Group.objects.get(name='П-62'))
            # elif group == 'П-63':
            #     user.groups.add(Group.objects.get(name='П-63'))
            # elif group == 'П-64':
            #     user.groups.add(Group.objects.get(name='П-64'))
            # elif group == 'П-65':
            #     user.groups.add(Group.objects.get(name='П-65'))
            # elif group == 'МФ-71':
            #     user.groups.add(Group.objects.get(name='МФ-71'))
            # elif group == 'МФ-72':
            #     user.groups.add(Group.objects.get(name='МФ-72'))
            # elif group == 'МФ-81':
            #     user.groups.add(Group.objects.get(name='МФ-81'))
            # elif group == 'МФ-82':
            #     user.groups.add(Group.objects.get(name='МФ-82'))
            # elif group == 'МФ-9':
            #     user.groups.add(Group.objects.get(name='МФ-9'))
            # elif group == 'МФ-10':
            #     user.groups.add(Group.objects.get(name='МФ-10'))
            # elif group == 'М-11':
            #     user.groups.add(Group.objects.get(name='М-11'))
            # elif group == 'Ф-11':
            #     user.groups.add(Group.objects.get(name='Ф-11'))
            # elif group == 'Х-71':
            #     user.groups.add(Group.objects.get(name='Х-71'))
            # elif group == 'Х-72':
            #     user.groups.add(Group.objects.get(name='Х-72'))
            # elif group == 'Х-81':
            #     user.groups.add(Group.objects.get(name='Х-81'))
            # elif group == 'Х-82':
            #     user.groups.add(Group.objects.get(name='Х-82'))
            # elif group == 'Х-9':
            #     user.groups.add(Group.objects.get(name='Х-9'))
            # elif group == 'Х-10':
            #     user.groups.add(Group.objects.get(name='Х-10'))
            # elif group == 'Х-11':
            #     user.groups.add(Group.objects.get(name='Х-11'))

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


@login_required
def currenttasks(request):

    materials = StudyMaterial.objects.all()

    return render(request, 'DNAcon/currenttasks.html', {'materials': materials})



@login_required
def user_files(request):
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            form = UserFileForm()

    else:
        form = UserFileForm()

    user_files = UserFile.objects.filter(user=request.user)
    return render(request, 'DNAcon/user_files.html', {'form': form, 'user_files': user_files})



@login_required
def delete_file(request, file_id):
    user_file = get_object_or_404(UserFile, id=file_id)

    if user_file.user == request.user:
        user_file.delete()

    return redirect('user_files')
