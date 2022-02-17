from django.contrib import messages, auth
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username):
                messages.error(request, 'Username is taken!')
                return redirect(reverse('account:register'))
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email is beigin used!')
                    return redirect(reverse('account:register'))
                else:
                    # password = make_password(password)
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect(reverse('account:login'))

        else:
            messages.error(request, 'Passwords do not match!')
            return redirect(reverse('account:register'))

        # return redirect(reverse('pages:index'))
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect(reverse('account:dashboard'))
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(reverse('account:login'))
    return render(request, 'accounts/login.html')


def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
