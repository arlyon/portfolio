from django.db import models

class Project(models.Model):
    link = models.URLField()
    source = models.URLField()
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250)
    display = models.BooleanField()
    imageurl = models.CharField(max_length=50)
