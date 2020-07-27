from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class ProfileModel(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bloodgroup = models.CharField(max_length=100, blank=True)
	mobile = models.CharField(max_length=10, blank=True)
	other_mobile = models.CharField(max_length=10, blank=True)
	address = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	zipcode = models.CharField(max_length=6, blank=True)
	avilable = models.CharField(max_length=100, blank=True)
	district = models.CharField(max_length=100, blank=True)
	birthdate = models.CharField(max_length=11, blank=True)
	pic=models.ImageField(upload_to='image/profile/', default='image/picd/default.jpg')

	
	class Meta:
		verbose_name = 'profile'
		verbose_name_plural = 'profiles'
	
	def __str__(self):
		return self.user.username

