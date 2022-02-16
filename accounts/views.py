from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Error')
        # return redirect(reverse('pages:index'))
    return render(request, 'accounts/register.html')


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    return redirect(reverse('pages:index'))
    
