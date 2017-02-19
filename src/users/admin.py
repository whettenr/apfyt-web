from django.contrib import admin


from .models import Company, CompanyApfytManager, Customer

admin.site.register(Company)
admin.site.register(CompanyApfytManager)
admin.site.register(Customer)

