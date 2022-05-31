from django.test import TestCase
from .models import category, Image, Location

# Create your tests here.
  
  
class categoryTestClass(TestCase):
    def setUp(self):
        self.love = category(cat_name= 'love')
    def test_instance(self):
        self.assertTrue(isinstance(self.love, category ))
class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(location_name= 'nairobi')
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location) )
class ImageTestClass(TestCase):
    def setUp(self):
        self.love = category(cat_name= 'love')
        self.love.save_category()
        self.nairobi = Location(location_name= 'nairobi')
        self.nairobi.save_location()
        self.imageVic = Image(name= "vic", description= "i love programming",image ="vics", pub_date= "2/2/2222",categoryName= self.love, location=self.nairobi )
    def test_instance(self):
        self.assertTrue(isinstance(self.imageVic , Image))
        
    def test_save_method(self):
        self.imageVic.save_image()
        editors = Image.objects.all()
        self.assertTrue(len(editors) > 0)
         
