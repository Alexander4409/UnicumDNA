from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)

    # Определите список доступных групп
    GROUP_CHOICES = (
        ('ИП-64', 'ИП-64'),
        ('ИП-65', 'ИП-65'),
        ('Р-71', 'Р-71'),
        # Добавьте другие группы по аналогии
    )

    # Используйте ChoiceField для выбора группы
    group = forms.ChoiceField(choices=GROUP_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'phone_number', 'group']

        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})

