from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('dashboard')

    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is being used')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'You are now registered and can log in')
        return redirect('login')

    return render(request, 'users/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'You are now logged out')
        return redirect('index')


def profile(request):
    return render(request, 'users/profile.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')
