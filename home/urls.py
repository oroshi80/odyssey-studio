from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Maps '/' to the home page
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),  
]
