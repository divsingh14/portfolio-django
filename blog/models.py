from django.db import models

class Blog(models.Model):
    title = models .CharField(max_length=255)
    pubDate = models.DateField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
