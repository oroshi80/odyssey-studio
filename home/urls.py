from django.urls import path
from .views import home, about, contact  # Changed from index to home

urlpatterns = [
    path('', home, name='index'),  # Maps '/' to the home page
    path('about', about, name='about'),
    path('contact', contact, name='contact')
]
