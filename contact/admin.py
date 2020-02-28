from django.contrib import admin

# Register your models here.
from .models import contact,bloodrequest


    
class cantactAdmin(admin.ModelAdmin):
    list_display = ['name','email','massage']

class bloodrequestAdmin(admin.ModelAdmin):
    list_display = ['name','bloodgroup', 'email','mobile','address','city','district', 'state']
    
admin.site.register(contact,cantactAdmin)
admin.site.register(bloodrequest,bloodrequestAdmin)
