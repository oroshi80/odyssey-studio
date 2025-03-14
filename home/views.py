from django.shortcuts import render, redirect
from datetime import datetime
from .forms import ContactForm

# Global var
current_year = datetime.now().year  # Get the current year (Globally)

# render page 
def home(request):
    return render(request, 'index.html', {
        'current_year': current_year,
        'active_page': 'home'  # Combine both into a single dictionary
    })

def about(request):
    return render(request, 'about.html', {
         'current_year': current_year,
        'active_page': 'about'
    })

def contact(request):
    # Check if the request is a POST
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract user data and save the contact
            user_ip = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT')

            contact = form.save(commit=False)
            contact.user_ip = user_ip
            contact.user_agent = user_agent
            contact.captcha_verified = True  # assuming you have a CAPTCHA system
            contact.save()

            # Redirect or show a success message
            return redirect('success')
        else:
            # Handle form errors
            return render(request, 'contact.html', {'form': form, 'current_year': current_year, 'active_page': 'contact'})

    else:
        form = ContactForm()

    # Render the contact form page
    return render(request, 'contact.html', {
        'form': form,
        'current_year': current_year,
        'active_page': 'contact'
    })

def success(request):
    return render(request, 'success.html')