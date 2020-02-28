from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=100, blank=True)
    email= models.CharField(max_length=100, blank=True)
    massage = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name


class bloodrequest(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    bloodgroup = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address =models.CharField(max_length=300, blank=True)

def __str__(self):
        return self.name