from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, label="Номер телефона")

    # Определите список доступных групп
    GROUP_CHOICES = (
        ('ИП-64', 'ИП-64'),
        ('ИП-65', 'ИП-65'),
        ('Р-71', 'Р-71'),
        # Добавьте другие группы по аналогии
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
