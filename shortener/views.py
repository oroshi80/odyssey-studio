from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from .forms import URLForm

# Create your views here.
def home(request): 
    form = URLForm()
    short_url = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url_instance = form.save()  # Save new short URL
            short_url = request.build_absolute_uri(f'/{url_instance.short_code}')
    
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code)
    url_instance.clicks += 1  # Track visits
    url_instance.save()
    return redirect(url_instance.original_url)