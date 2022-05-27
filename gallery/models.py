from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length= 40)
    