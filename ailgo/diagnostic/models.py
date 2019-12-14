from __future__ import unicode_literals

from django.db import models
from profiles.models import User
from doctor.models import Doctor
from contact.models import Contacts, Locality, City
from datetime import *


# Create your models here.
class Test(models.Model):
	test_name = models.CharField(max_length = 100)
	cost = models.IntegerField()


class Pathalogy(models.Model):
    name = models.CharField(max_length = 100)
    contact = models.ForeignKey(Contacts)
    reg_date = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=False)
    working_since = models.IntegerField(default = 1)
    is_sponsered = models.BooleanField(default = True)
    percent = models.FloatField(null=True,blank=True)
    test_supported =  models.ManyToManyField(Test, blank=True)

class TestRecord(models.Model):
	user = models.ForeignKey(User)
	tests = models.ForeignKey(Test)
	pathology = models.ForeignKey(Pathalogy)
	doctor = models.ForeignKey(Doctor)
	conducted_on = models.DateTimeField(default = datetime.now)
