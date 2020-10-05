from django.db import models

# Create your models here.
from django.urls import reverse


class test(models.Model):
    username=models.TextField(max_length=50)
    userid=models.IntegerField(max_length=255)

