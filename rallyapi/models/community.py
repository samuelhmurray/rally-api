from django.db import models
from location_field.models.plain import PlainLocationField

class Community(models.Model):
    name = models.CharField(max_length=100)
    location = PlainLocationField()
