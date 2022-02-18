from audioop import reverse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            listing_id = request.POST['listing_id']
            user_id = request.user.id
            if Contact.objects.filter(listing_id=listing_id, user_id=user_id):
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect(f'/listing/{listing_id}')
            else:
                Contact.objects.create(
                    user_id=request.POST.get('user_id', None),
                    listing=request.POST.get('listing', None),
                    name=request.POST.get('name', None),
                    email=request.POST.get('email', None),
                    phone=request.POST.get('phone', None),
                    message=request.POST.get('message', None),
                    listing_id=listing_id
                )
            messages.success(
                request, 'Your request has been submitted, a realtor will get back to you soon')
            # send_mail(
            #     'Property Listing Inquiry',
            #     f'There has been an inquiry for {request.POST["listing"]}. Sign into the admin panel for more info',
            #     'peidrao01@gmail.com',
            #     [request.POST['realtor_email'], 'peidrao01@gmail.com'],
            #     fail_silently=False
            # )
        return redirect(f'/listing/{listing_id}')
