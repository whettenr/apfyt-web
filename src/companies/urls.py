from django.conf.urls import url

from .views import company_profile, DealOfTheDayListView 

urlpatterns = [
    url(r'^$', company_profile, name='company_profile'),
    url(r'^edit/$', company_profile, name='company__edit_profile'),
    url(r'^dotd/$', DealOfTheDayListView.as_view(), name='deal_list'),
    ]