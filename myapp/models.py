from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField()
    confirmpass=models.CharField()

class Query(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    query=models.TextField()