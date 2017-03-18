from django.conf.urls import url

from .views import company_profile, CompanyProfileEditView, DealOfTheDayListView 

urlpatterns = [
    url(r'^$', company_profile, name='company_profile'),
    url(r'^edit/$', CompanyProfileEditView.as_view(), name='company_edit_profile'),
    url(r'^dotd/$', DealOfTheDayListView.as_view(), name='deal_list'),
    ]