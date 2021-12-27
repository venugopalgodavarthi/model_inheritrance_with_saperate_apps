from django.db import models

# Create your models here.
class dept(models.Model):
    dname=models.CharField(max_length=40)
    location = models.CharField(max_length=50)  
    def __str__(self):
        return self.dname
    
class employee(dept):
    firstname=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=150)
    aadhar=models.BigIntegerField()
    li=[['account','ACCOUNT'],['manager','MANAGER']]
    d=models.CharField(max_length=50, choices=li)