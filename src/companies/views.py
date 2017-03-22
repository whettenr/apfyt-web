from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.forms.widgets import SelectDateWidget
from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .mixins import CompanyManagerStatusRequiredMixin, CompanyManagerEditStatusRequiredMixin
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

class CompanyProfileEditView(CompanyManagerStatusRequiredMixin, UpdateView):

	model = Company
	fields = '__all__'
	template_name_suffix = '_edit_profile'
	success_url = '/company/'

	def get_object(self):
		company = self.request.user.companyapfytmanager.company
		return company


class DealOfTheDayListView(CompanyManagerStatusRequiredMixin, ListView):
	model = DealOfTheDay

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

class DealOfTheDayCreateView(CompanyManagerEditStatusRequiredMixin, CreateView):
	model = DealOfTheDay

# class DealOfTheDayDeleteView():

class DealOfTheDayDetailView(CompanyManagerStatusRequiredMixin, DetailView):
	model = DealOfTheDay

	# I belive we'd want to diplay certain info or
	# data about how a particular deal has been used
	# do to this id add on the the get_context data like this

	# def get_context_data(self, **kwargs):
	# 	context = super(DealOfTheDayDetailView, self).get_context_data(**kwargs)
	#	# ex.) add the variable 'now' that will be sent to html
	# 	context['now'] = timezone.now()
	#	# ex.) maybe each time the ios app views a deal we can record it 
	#	#      and then have a var like this
	# 	# context['number_of_view'] = 10 
	# 	return context

	def get_object(self, *args, **kwargs):
		deal = super(DealOfTheDayDetailView, self).get_object(*args, **kwargs)
		if deal.company != self.request.user.companyapfytmanager.company:
			raise Http404
		return super(DealOfTheDayDetailView, self).get_object(*args, **kwargs)



class DealOfTheDayEditView(CompanyManagerEditStatusRequiredMixin, UpdateView):
	model = DealOfTheDay
	form_class =  modelform_factory(
		DealOfTheDay,
		fields = {'name', 'start_date', 'expiration_date', 'image', 'cropping', 'active' },
        widgets={'start_date': SelectDateWidget, 'expiration_date': SelectDateWidget }
        )

	# overide get_object to validate that the deal of the day
	# and the user are from the same company
	# i.e. we dont want people from other companies editing a 
	# different companies information
	def get_object(self, *args, **kwargs):
		deal = super(DealOfTheDayEditView, self).get_object(*args, **kwargs)
		if deal.company != self.request.user.companyapfytmanager.company:
			raise Http404
		return super(DealOfTheDayEditView, self).get_object(*args, **kwargs)




