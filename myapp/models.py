from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField()
    confirmpass=models.CharField()
    profile=models.ImageField(upload_to='file/',null=True)

class Query(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    query=models.TextField()