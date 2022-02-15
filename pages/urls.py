from django.urls import path
from .views import index, about, search

app_name='pages'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('search/', search, name='search')
]
