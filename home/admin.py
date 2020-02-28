from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import reportdoner,bloodbank,event,sliderimg

class ReportAdmin(admin.ModelAdmin):
    list_display = ['reportuseracc','mail','mobile','reason','reportinfo']
    
class bankAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','state','district','city','address']

class eventAdmin(admin.ModelAdmin):
    list_display = ['title','summry','date','pic']

class slideAdmin(admin.ModelAdmin):
    list_display = ['summry','pic',]
    
admin.site.register(reportdoner,ReportAdmin)
admin.site.register(bloodbank,bankAdmin)
admin.site.register(event,eventAdmin)
admin.site.register(sliderimg,slideAdmin)
