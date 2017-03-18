from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from .mixins import CompanyManagerStatusRequiredMixin
from .models import Company, DealOfTheDay


# person must be logged in
@login_required
def company_profile(request):
	# verifies that the user is associated with a company
	try:
		request.user.companyapfytmanager
	except:
		raise Http404

	# context is the data that gets passed to the html template
	# we should gather data here and then add it to the template
	context = {
		"company": request.user.companyapfytmanager.company,
	}

	return render(request,'companies/company_profile.html', context)


class DealOfTheDayListView(CompanyManagerStatusRequiredMixin, ListView):
	model= DealOfTheDay

	# def get(self, request, *args, **kwargs):
	# 	# verifies that the user is associated with a company
	# 	# maybe we should develope a company login
	# 	# i don't like the idea of just raising and http 404 error 
	# 	# i think it should redirect them to a login
	# 	try:
	# 		request.user.companyapfytmanager
	# 	except:
	# 		raise Http404

	# 	return super(DealOfTheDayListView, self).get(request, *args, **kwargs)
	
	def get_queryset(self):
		return super(DealOfTheDayListView, self).get_queryset().filter(company=self.request.user.companyapfytmanager.company)


class CompanyProfileEditView(CompanyManagerStatusRequiredMixin, UpdateView):

	model = Company
	# template_name = "companies/company_edit_profile.html"
	fields = '__all__'
	template_name_suffix = '_edit_profile'
	success_url = '/company/'

	def get_object(self):
		company = self.request.user.companyapfytmanager.company
		return company



