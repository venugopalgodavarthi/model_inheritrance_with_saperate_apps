from django.contrib import admin
from demo2.models import adminstration,Student,Trainers
# Register your models here.

class Traineradmin(admin.ModelAdmin):
    list_display=['id','surname','firstname', 'email', 'phone', 'address', 'aadhar','design','domain','salary' ]
    
class studentadmin(admin.ModelAdmin):
    list_display=['id','surname','firstname', 'email', 'phone', 'address', 'aadhar','course','marks','cost' ]

class adminstrationadmin(admin.ModelAdmin):
    list_display=['id','surname','firstname', 'email', 'phone', 'address', 'aadhar','dno','street','city','state',
                  'country']


admin.site.register(adminstration,adminstrationadmin)
admin.site.register(Student,studentadmin)
admin.site.register(Trainers,Traineradmin)
