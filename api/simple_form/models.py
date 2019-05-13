from django.db import models


# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

