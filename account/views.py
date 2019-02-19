from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, ProfileForm, UserEditForm, ProfileEditForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user_id = new_user.pk
            new_profile.save()
            cd = user_form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
            return render(request, 'account/profile.html',
                          {'new_user': new_user, 'new_profile':new_profile})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'account/register.html',
                  {'user_form': user_form, 'profile_form': profile_form})
#процесс регистрации позьзователей


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST, files=request.FILES)
        if all([user_form.is_valid(), profile_form.is_valid()]):
            user_form.save()
            profile_form.save()
            return render(request, 'account/profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,'account/edit_profile.html',
                      {'user_form': user_form, 'profile_form': profile_form})
#редактирование информации в своем профиле и фотографии


def other_profile(request,u_name):
    if request.user.username == u_name:
        return render(request, 'account/profile.html', )
    else:
        other_user=get_object_or_404(User, username=u_name)
        return render(request, 'account/other_profile.html',
                      {'other_user': other_user})
#просмотр чужого профиля


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/login.html',
                                  {'user':user})
                else:
                    message='Аккаунт отключен'
                    form = LoginForm()
                    return render(request, 'account/login.html',
                                  {'form': form, 'message': message})
            else:
                message='Не верное имя пользователя или пароль'
                form = LoginForm()
                return render(request, 'account/login.html',
                              {'form': form, 'message': message})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
#вход в учетную запись пользователя


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
#выход из учетной записи


def profile(request):
    return render(request, 'account/profile.html',)
#просмотр своего профиля
