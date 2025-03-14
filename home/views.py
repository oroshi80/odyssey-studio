from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    current_year = datetime.now().year  # Get the current year
    return render(request, 'index.html', {
        'current_year': current_year,
        'active_page': 'home'  # Combine both into a single dictionary
    })

def about(request):
    return render(request, 'about.html', {'active_page': 'about'})

def contact(request):
    return render(request, 'contact.html', {'active_page': 'contact'})
