from django.shortcuts import render

from listings.choices import bedroom_choices, price_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.filter(
        is_published=True).order_by('-list_date')[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,

    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'realtors': Realtor.objects.order_by('-hire_date'),
        'mvp_realtors': Realtor.objects.filter(is_mvp=True)
    }
    return render(request, 'pages/about.html', context)


def search(request):
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/search.html', context)
