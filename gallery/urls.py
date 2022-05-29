from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', views.home, name = 'home'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^category/', views.categories, name= "categories"),
    re_path(r'^location/', views.location, name='location'),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)