# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser
