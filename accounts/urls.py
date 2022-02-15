from django.urls import path
from .views import login, register, dashboard, logout

app_name='account'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout')
]
