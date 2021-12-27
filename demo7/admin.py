from django.contrib import admin

from demo7.models import customer, product, transcation

# Register your models here.


class customeradmin(admin.ModelAdmin):
    list_display=['cid','name','email','phone','address','adhaar']

class productadmin(admin.ModelAdmin):
    list_display=['pid','pname','pdesc','price',]
    
class transcationadmin(admin.ModelAdmin):
    list_display=['tid','cust_id','prod_id','totalprice','date']

admin.site.register(customer,customeradmin)
admin.site.register(product,productadmin)
admin.site.register(transcation,transcationadmin)
