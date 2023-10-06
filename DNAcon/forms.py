from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, label="Номер телефона")

    # Определите список доступных групп
    GROUP_CHOICES = (
        # ('ИП-50', 'ИП-50'),
        # ('ИП-51', 'ИП-51'),
        # ('ИП-52', 'ИП-52'),
        # ('ИП-53', 'ИП-53'),
        # ('ИП-54', 'ИП-54'),
        # ('ИП-55', 'ИП-55'),
        # ('ИП-61', 'ИП-61'),
        # ('ИП-62', 'ИП-62'),
        # ('ИП-63', 'ИП-63'),
        ('ИП-64', 'ИП-64'),
        ('ИП-65', 'ИП-65'),
        # ('ИЭ-71', 'ИЭ-71'),
        # ('ИЭ-72', 'ИЭ-72'),
        # ('ИЭ-81', 'ИЭ-81'),
        # ('ИЭ-82', 'ИЭ-82'),
        # ('ИЭ-9', 'ИЭ-9'),
        # ('ИЭ-10', 'ИЭ-10'),
        # ('ИЭ-11', 'ИЭ-11'),
        # ('Р-71', 'Р-71'),
        # ('Р-72', 'Р-72'),
        # ('Р-81', 'Р-81'),
        # ('Р-82', 'Р-82'),
        # ('Р-9', 'Р-9'),
        # ('Р-10', 'Р-10'),
        # ('ИИ-71', 'ИИ-71'),
        # ('ИИ-72', 'ИИ-72'),
        # ('ИИ-81', 'ИИ-81'),
        # ('ИИ-82', 'ИИ-82'),
        # ('ИИ-9', 'ИИ-9'),
        # ('ИИ-10', 'ИИ-10'),
        # ('ИИ-11', 'ИИ-11'),
        # ('П-51', 'П-51'),
        # ('П-52', 'П-52'),
        # ('П-53', 'П-53'),
        # ('П-54', 'П-54'),
        # ('П-55', 'П-55'),
        # ('П-61', 'П-61'),
        # ('П-62', 'П-62'),
        # ('П-63', 'П-63'),
        # ('П-64', 'П-64'),
        # ('П-65', 'П-65'),
        # ('МФ-71', 'МФ-71'),
        # ('МФ-72', 'МФ-72'),
        # ('МФ-81', 'МФ-81'),
        # ('МФ-82', 'МФ-82'),
        # ('МФ-9', 'МФ-9'),
        # ('МФ-10', 'МФ-10'),
        # ('М-11', 'М-11'),
        # ('Ф-11', 'Ф-11'),
        # ('Х-71', 'Х-71'),
        # ('Х-72', 'Х-72'),
        # ('Х-81', 'Х-81'),
        # ('Х-82', 'Х-82'),
        # ('Х-9', 'Х-9'),
        # ('Х-10', 'Х-10'),
        # ('Х-11', 'Х-11'),
    )

    group = forms.ChoiceField(choices=GROUP_CHOICES, required=True, label="Группа")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'phone_number', 'group']

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Номер телефона',
            'group': 'Группа',
            'username': 'Имя пользователя',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})


# forms.py

from django import forms
from .models import UserFile

class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ('uploaded_file',)

        labels = {
            'uploaded_file':'Загрузите файл'
        }
