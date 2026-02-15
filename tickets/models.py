from django.db import models
from datetime import datetime


# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    status = models.CharField(choices=(("1", "Pendiente"), ("2", "En Desarrollo"), ("3", "Finalizado")), default="1", max_length=30)
    contact_info = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
