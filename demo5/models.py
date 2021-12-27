from django.db import models

# Create your models here.

class details(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    adhaar=models.BigIntegerField()
    def __str__(self):
        return self.name
    
class student(details):
    li=[['Python','PYTHON'],['Testing','TESTING'],['DataScience','DATASCIENCE']]
    course=models.CharField(max_length=50,choices=li)
    marks=models.IntegerField()
    fee=models.FloatField()
    
class facutly(details):
    li=[['Python full stack','PYTHON FULL STACK'],['Python Testing','PYTHON TESTING'],['Python DataScience','PYTHON DATASCIENCE']]
    course=models.CharField(max_length=100,choices=li)
    salary=models.FloatField()
    
    
    