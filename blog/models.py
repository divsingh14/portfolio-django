from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubDate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pubDatePretty(self):
        time = datetime.now()
        if self.pubDate.day == time.day:
              return str(time.hour - self.pubDate.hour) + " hours ago"
        else:
            if self.month == time.month:
                return str(time.day - self.pubDate.day) + " days ago"

        return self.pubDate