from django.db import models
class student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname=models.CharField(max_length=150)
    marks=models.IntegerField(null=True)
    doj=models.DateField(default="1995-06-06")
    def __str__(self):
        return self.sname
    
class sample(models.Model):
    sid1=models.IntegerField()
    sid2=models.BigAutoField(primary_key=True)
    sid3=models.BigIntegerField()
    sid4=models.FloatField()
    sid5=models.DecimalField(decimal_places=5,max_digits=5)
    sid6=models.DurationField()
    sname3=models.BooleanField()
    ip=models.GenericIPAddressField()
    ip1=models.BinaryField()
    
    date1=models.DateField()
    date2=models.DateTimeField()
    date3=models.TimeField()
    
    sname=models.CharField(max_length=150)
    sanme1=models.URLField(max_length=150)
    sname2=models.UUIDField(max_length=150)
    email=models.EmailField(max_length=150)
    img=models.ImageField()
    
    