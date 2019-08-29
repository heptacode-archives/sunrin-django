from django.db import models

# Create your models here.
class Sruser(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    registerd = models.DateTimeField(auto_now_add=True)