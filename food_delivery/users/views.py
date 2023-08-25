from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# from .utils import search_profiles, paginate_profiles


def login_user(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Такого пользователя не существует")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, "Имя пользователя или пароль некорректны")

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Пользователь был разлогинен!')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Аккаунт пользователя создан!')
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, "При регистрации произошла ошибка")

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    context = {
        'profile': prof
    }
    return render(request, 'good_food/projects.html', context)