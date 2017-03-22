from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from image_cropping.fields import ImageCropField, ImageRatioField


# Create your models here.
def image_upload_to_company_folder(instance, filename):
	name = instance.name
	slug = slugify(name)
	
	return "images/%s/%s" %(slug, filename)


class Company(models.Model):
	name = models.CharField(max_length=25)
	bio = models.TextField(max_length=500, blank=True)
	profile_image = ImageCropField(upload_to=image_upload_to_company_folder, blank=True, null=True)
	cropping = ImageRatioField('profile_image', '600x600', allow_fullsize=True)

	
	def __unicode__(self): #def __str__(self):
		return self.name

class DealOfTheDay(models.Model):
	name = models.CharField(max_length=25)
	company = models.ForeignKey(Company)
	image = ImageCropField(upload_to='images/dotd/')
	cropping = ImageRatioField('image', '600x600', allow_fullsize=True)
	active = models.BooleanField(default=True)

	removed = models.BooleanField(default=False)
	# we need to add validation to prevent the creation of
	# a deal where start_data > expiration_date
	start_date = models.DateField(blank=True, null=True)
	expiration_date = models.DateField(blank=True, null=True)

	# add integer field
	# cropping_free = ImageRatioField('image_field', '300x230', free_crop=True, size_warning=True)
	

	def get_absolute_url(self):
		return reverse('dotd_detail', kwargs={'pk': self.pk})

	def __unicode__(self): #def __str__(self):
		return self.name
