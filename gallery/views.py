from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):   
    images = Image.all_images()
    return render(request, 'index.html', {"images": images}  )