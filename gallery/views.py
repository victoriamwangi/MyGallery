from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, category, Location
from django.db.models import Q

# Create your views here.
def home(request):   
    images = Image.all_images().order_by('-pub_date')
    return render(request, 'index.html'  , {"images": images})
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
def categories(request):
    categories = category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'category.html', context)    

def location(request):
    location = Location.objects.all()

    context = {
        'locations': location,
    }
    return render(request, 'location.html', context) 
    
    
    
