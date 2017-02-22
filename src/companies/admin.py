from django.contrib import admin
from image_cropping import ImageCroppingMixin


from .models import Company, DealOfTheDay

class DealOfTheDayAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Company)
admin.site.register(DealOfTheDay, DealOfTheDayAdmin)
