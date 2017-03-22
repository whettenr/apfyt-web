from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from companies.models import Company


class CompanyApfytManager(models.Model):
	company = models.ForeignKey(Company)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	edit_permission = models.BooleanField(default=False)

	def __unicode__(self): #def __str__(self):
		return str(self.company) + " " + str(self.user)


# im thinking this model is not necessary
# django/facebook authentication already collects 
# and stores all the data 

# class ApfytUser(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	birth_year = models.DateField()

