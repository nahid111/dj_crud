from django.shortcuts import render, redirect
from django.contrib import auth, messages


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        messages.error(request, f'{email} {password}')
        messages.warning(request, f'{email} {password}')
        messages.success(request, f'{email} {password}')
        messages.info(request, f'{email} {password}')
        return redirect('login')
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        print(email, password, confirm_password)
        return redirect('register')
    return render(request, 'users/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def profile(request):
    return render(request, 'users/profile.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')
