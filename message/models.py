from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=255)
    nim = models.IntegerField(max_length=10)
    messages = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)