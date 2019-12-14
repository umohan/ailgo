from __future__ import unicode_literals

from django.db import models
from datetime import *

# Create your models here.
TYPE = ((1,'user'), (2,'doctor'), (3,'pathology'))

class City(models.Model):
	name = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	country = models.CharField(max_length = 50)

class Locality(models.Model):
	name = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	city = models.ForeignKey(City)

class Contacts(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on =  models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=20)
	mobile = models.IntegerField()
	alt_mobile = models.IntegerField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	email2 = models.EmailField(null=True, blank=True)
	permanent_address = models.TextField(null=True, blank=True)
	current_locality = models.ForeignKey(Locality)
	user_type = models.IntegerField(choices=TYPE, default=1)

