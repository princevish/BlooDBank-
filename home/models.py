from django.db import models
from datetime import datetime
from accounts.models import ProfileModel



# Create your models here.
class reportdoner(models.Model):

    reportuseracc = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    mail = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    reason = models.CharField(max_length=100, blank=True)
    reportinfo = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.reportuseracc.user.username

		
class bloodbank(models.Model):
    name= models.CharField(max_length=100, blank=True)
    state= models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=300, blank=True) 
    mobile = models.CharField(max_length=20, blank=True) 
    def __str__(self):
        return self.state


class event(models.Model):
    title = models.CharField(max_length=100, blank=True)
    summry = models.TextField(max_length=500, blank=True)
    date=models.DateTimeField(auto_now=True)
    pic=models.ImageField(upload_to='image/event/', default='image/picd/default.jpg')

    def __str__(self):
        return self.title

class sliderimg(models.Model):

    summry = models.TextField(max_length=500, blank=True)

    pic=models.ImageField(upload_to='image/slide/', default='image/picd/default.jpg')

    def __str__(self):
        return self.summry