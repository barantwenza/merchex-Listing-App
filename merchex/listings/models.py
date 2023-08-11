from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

class TitlesBand(models.Model):
    title = models.fields.CharField(max_length=200)
    
#Create your models here.
