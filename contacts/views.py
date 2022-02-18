from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            user_id=request.POST.get('user_id', None),
            listing=request.POST.get('listing', None),
            name=request.POST.get('name', None),
            email=request.POST.get('email', None),
            phone=request.POST.get('phone', None),
            message=request.POST.get('message', None),
            listing_id=request.POST.get('listing_id', None)
        )
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect(f'/listing/{request.POST["listing_id"]}')
