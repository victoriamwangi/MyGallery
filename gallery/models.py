from django.db import models
import datetime as dt


class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length= 40)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    categoryName = models.ForeignKey('category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    
    def save_image(self): 
        self.save() 
    def delete_image(self): 
        self.delete() 
    
    @classmethod
    def all_images(cls): 
        images= Image.objects.all() 
        return images
    
    @classmethod
    def search_by_category(cls, search_term):
        posts = cls.objects.filter(cat_name__icontains=search_term)
        return posts

    def __str__(self): 
        return self.name 
     
class Location(models.Model):
    location_name = models.CharField(max_length=20) 
   
    
    def save_location(self): 
        self.save() 
    def delete_location(self): 
        self.delete() 
    def __str__(self): 
        return self.location_name 
 
class category(models.Model):
    cat_name =models.CharField(max_length=20)
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def search_by_category(cls, search_term):
        posts = cls.objects.filter(cat_name__icontains=search_term)
        return posts
    
    def __str__(self):
        return self.cat_name
    
  

     