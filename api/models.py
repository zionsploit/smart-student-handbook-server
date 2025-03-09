from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()