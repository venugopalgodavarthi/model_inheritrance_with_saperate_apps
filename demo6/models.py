from django.db import models

# Create your models here.


class customer(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    adhaar=models.BigIntegerField()
    def __str__(self):
        return self.name
    
class product(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=100)
    price=models.BigIntegerField()
    def __str__(self):
        return self.pname

class transcation(customer,product):
    tid = models.AutoField(primary_key=True)
    totalprice=models.FloatField()
    date=models.DateField()
    def __str__(self):
        return str(self.tid)
     
    
    
