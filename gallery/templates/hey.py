from django.db import models import datetime as dt class Location(models.Model):
location_name = models.CharField(max_length=20) location_code =
models.CharField(max_length=48) def save_location(self): self.save() def
delete_location(self): self.delete() def __str__(self): return
self.location_name class Category(models.Model): category_name =
models.CharField(max_length =30) def __str__(self): return self.category_name
def save_category(self): self.save() def delete_category(self): self.delete()
def __str__(self): return self.category_name class Image(models.Model): name =
models.CharField(max_length=20) description = models.CharField(max_length= 40)
image = models.ImageField(upload_to = 'images/', null=True, blank=True) pub_date
= models.DateTimeField(auto_now_add=True) # location =
models.ForeignKey(Location, on_delete=models.CASCADE) category =
models.ForeignKey(Category,on_delete=models.CASCADE) trial =
models.CharField(max_length=30) def save_image(self): self.save() def
delete_image(self): self.delete() @classmethod def all_images(cls): images=
Image.objects.all() return images def __str__(self): return self.name
{%extends 'base.html'%} {% block content %}
<div class="container">
  <div class="row">
    {% if categories%} {% for category in categories %}
    <div class="col-sm-6 col-md-3">
      <h1>{{category.name}}</h1>
      <img class="card-img-top" src="{{category.image.url}}" alt="" />
    </div>
    {% endfor %} {% else %}
    <h2>Found 0 posts for the search term {{message}}</h2>
    {% endif %}
  </div>

  <div class="row"></div>
</div>
{% endblock %}