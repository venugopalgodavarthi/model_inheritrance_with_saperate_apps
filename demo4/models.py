from django.db import models

# Create your models here.

class stu(models.Model):
    firstname=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.firstname
    
class address(stu):
    dno=models.CharField(max_length=30)
    street=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=150)
    pin=models.IntegerField()
    def __str__(self):
        return self.city
class course(address):
    courses=models.CharField(max_length=30)
    marks=models.IntegerField()
    fee=models.IntegerField()
    
    
    
