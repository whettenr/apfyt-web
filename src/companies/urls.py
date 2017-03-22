from django.conf.urls import url

from .views import (
	company_profile, 
	CompanyProfileEditView, 
	DealOfTheDayListView,
	DealOfTheDayCreateView,
	# DealOfTheDayDeleteView,
	DealOfTheDayDetailView,
	DealOfTheDayEditView,
	) 

urlpatterns = [
    url(r'^$', company_profile, name='company_profile'),
    url(r'^edit/$', CompanyProfileEditView.as_view(), name='company_edit_profile'),

    url(r'^dotd/$', DealOfTheDayListView.as_view(), name='dotd_list'),
    url(r'^dotd/create/$', DealOfTheDayCreateView.as_view(), name='dotd_create'),
    #url(r'^dotd/delete/(?P<pk>\d+)/$', DealOfTheDayDeleteView.as_view(), name='dotd_delete'),
    # doesn't actuall delete, just removes from view
    url(r'^dotd/(?P<pk>\d+)/$', DealOfTheDayDetailView.as_view(), name='dotd_detail'),
    url(r'^dotd/(?P<pk>\d+)/edit/$', DealOfTheDayEditView.as_view(), name='dotd_edit'),

    ]