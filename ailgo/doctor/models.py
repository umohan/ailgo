from __future__ import unicode_literals

from django.db import models
from contact.models import Contacts


# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    contact = models.ForeignKey(Contacts)
    reg_date = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=False)
    experience = models.IntegerField(default = 0)