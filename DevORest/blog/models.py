from django.db import models
from datetime import date

class blog(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    data = models.DateField(default=date.today)
    descripion = models.TextField(null=True,blank=True)


