from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from companies.models import Company


class CompanyApfytManager(models.Model):
	company = models.ForeignKey(Company)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	
class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth_year = models.DateField()

