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
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }
    return render(request, 'pages/search.html', context)
