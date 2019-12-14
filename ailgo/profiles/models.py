from __future__ import unicode_literals

from django.db import models
from contact.models import Contacts, Locality, City
from datetime import *
from doctor.models import Doctor


GENDER = ( (1,'MALE'),
	(2, 'FEMALE'), 
	(3,'OTHER')
	)

class User(models.Model):
    aadhar = models.IntegerField()
    name = models.CharField(max_length = 100)
    contact = models.ForeignKey(Contacts)
    reg_date = models.DateTimeField(auto_now_add = True)
    is_working = models.BooleanField(default=False)
    gender = models.IntegerField(choices=GENDER, default=1)
    age = models.IntegerField(null = True, blank = True)

class Allergies(models.Model):
	name = models.CharField(max_length = 100)
	created_on = models.DateTimeField(auto_now_add = True)
	approx_duration_month = models.IntegerField(default = 2)
	is_active = models.BooleanField(default = True)
	user = models.ForeignKey(User)

class Medicines(models.Model):
	name = models.CharField(max_length = 100)
	days_to_take = models.IntegerField(default = 2)
	no_of_time = models.IntegerField(default = 2)
	starting_date = models.DateTimeField(default = datetime.now)
	is_active = models.BooleanField(default = False)

class Presciptions(models.Model):
	allergies = models.ManyToManyField(Allergies, blank=True)
	medicine = models.ManyToManyField(Medicines, blank = True)
	created_on = models.DateTimeField(auto_now_add = True)
	ailment = models.TextField(null=True, blank=True)
	user = models.ForeignKey(User)
	doctor = models.ForeignKey(Doctor)




