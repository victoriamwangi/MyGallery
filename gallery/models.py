from django.db import models
import datetime as dt


class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length= 40)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod
    def all_images(cls):
        images= Image.objects.all()
        return images
    
    def __str__(self):
        return self.name
    