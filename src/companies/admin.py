from django.contrib import admin
from image_cropping import ImageCroppingMixin


from .models import Company, DealOfTheDay

class CompanyAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass

class DealOfTheDayAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(DealOfTheDay, DealOfTheDayAdmin)
