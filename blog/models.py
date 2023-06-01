from django.db import models
import datetime

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='blog/images')
    date=models.DateField(datetime.date.today) 
    # el valor de fecha por defecto es datetime.date.today(fecha actual)