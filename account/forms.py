from django import forms
from django.contrib.auth.models import User
from . models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'city', 'dateOfBirth')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','city')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
