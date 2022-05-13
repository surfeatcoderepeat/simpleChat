from email import message
from pyexpat import model
from django.db import models
# from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)
    room = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
