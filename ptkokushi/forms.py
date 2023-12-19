from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models


class SignupForm(UserCreationForm):
    birth_date = forms.DateField(
        help_text='必須: YYYY-MM-DD 形式で入力して下さい。',
        label='誕生日',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

