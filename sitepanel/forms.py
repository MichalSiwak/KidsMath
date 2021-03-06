from django import forms
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class EditProfileForm(forms.Form):
    username = forms.CharField(label='login')
    first_name = forms.CharField(label='Imię', required=False)
    last_name = forms.CharField(label='Nazwisko', required=False)


class RegisterForm(UserCreationForm):

    class Meta:
        fields = ["username", "password1", "password2", "email"]
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input'
        self.fields['username'].label = 'Login'


class EditPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_password2'].label = _('Powtórz nowe hasło')


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Adres email', widget=forms.EmailInput(attrs={
        'class': 'input',
        'type': 'email',
        'name': 'email'
        }))


class PasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetConfirmForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='Nowe hasło', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'type': 'password',
        'name': 'new_password1',
    }))

    new_password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'type': 'password',
        'name': 'new_password2'
    }))

    def clean(self):
        cleaned_data = super().clean()
        print(self.error_messages)
        return cleaned_data


class ChangeEmailForm(ModelForm):

    class Meta:
        fields = ["password", "email"]
        model = User

    password = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'type': 'password',
        'name': 'new_password',
    }))

    email = forms.EmailField(label='Podaj nowy adres e-mail', widget=forms.EmailInput(attrs={
        'class': 'input',
        'type': 'email',
        'name': 'email'
        }))


class AddKidsForm(RegisterForm):
    class Meta:
        fields = ["username", "first_name", "last_name", "password1", "password2"]
        model = User

    def __init__(self, *args, **kwargs):
        self.parent = False
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input'
        self.fields['username'].label = 'Login'

    def save(self, *args, **kwargs):
        self.instance.parent = kwargs.pop('parent', None)
        super(AddKidsForm, self).save(*args, **kwargs)
