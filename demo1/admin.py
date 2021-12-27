from django.contrib import admin
from demo1.models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['sid','sname','marks','doj']
    
    
admin.site.register(student,studentadmin)
