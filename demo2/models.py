from django.db import models

# Create your models here.

class base(models.Model):
    surname=models.CharField(max_length=30)
    firstname=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=150)
    aadhar=models.BigIntegerField()
    class Meta:
        abstract=True
    def __str__(self):
        return self.firstname
    
class address(models.Model):
    dno=models.CharField(max_length=30)
    street=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=150)
    pin=models.IntegerField()
    class Meta:
        abstract=True
    
class Trainers(base):
    salary=models.FloatField()
    li=[['development','DEVELOPMENT'],['testing','TESTING']]
    design=models.CharField(max_length=50, choices=li)
    domain=models.CharField(max_length=50)  
    
class adminstration(base,address):
    salary=models.FloatField()
    li=[['account','ACCOUNT'],['manager','MANAGER']]
    design=models.CharField(max_length=50, choices=li)

class Student(base):
    cost=models.FloatField()
    li=[['python','PYTHON'],['manual','MANUAL'],['datascience','datascience']]
    course=models.CharField(max_length=50, choices=li)
    marks=models.CharField(max_length=50)    
      
