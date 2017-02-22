from __future__ import unicode_literals

from django.db import models
from image_cropping.fields import ImageCropField, ImageRatioField


# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=25)
	bio = models.TextField(max_length=500, blank=True)
	
	def __unicode__(self): #def __str__(self):
		return self.name

class DealOfTheDay(models.Model):
	name = models.CharField(max_length=25)
	company = models.ForeignKey(Company)
	image = models.ImageField(upload_to='images/dotd/')
	# add integer field

	cropping = ImageRatioField('image_field', '120x100', allow_fullsize=True)
	cropping_free = ImageRatioField('image_field', '300x230', free_crop=True, size_warning=True)
	
	def __unicode__(self): #def __str__(self):
		return self.name
