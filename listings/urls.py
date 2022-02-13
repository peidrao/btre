from django.urls import path

from .views import listing, listings, search

app_name = 'listings'

urlpatterns = [
    path('', listings, name='listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search', search, name='search')
]
