from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField()
    confirmpass=models.CharField()
    profile=models.ImageField(upload_to='file/',null=True)


#......................Qurry model.............................................
class Query(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    query=models.TextField()

#..........................Admin model............................................

class Productinfo(models.Model):
    pro_name=models.CharField(max_length=30)
    pro_price=models.IntegerField()
    pro_disc=models.CharField(max_length=100,null=True)
    pro_image=models.ImageField(upload_to='file')
    pro_mrp=models.IntegerField(null=True) 


# ...........................payement.................................................

class Payment(models.Model):
    user_id=models.IntegerField()
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True)
    signature = models.CharField(max_length=255, blank=True)
    amount = models.IntegerField()  
    status = models.CharField(max_length=20, default="Created")  
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        db_table='Payment'

#.............................Address model...........................................

class Address(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    address1=models.CharField()
    address2=models.CharField()
    zip=models.IntegerField()
    city=models.CharField()
