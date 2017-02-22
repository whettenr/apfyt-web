from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import DealOfTheDay

def company_profile(request):
	# verifies that the user is associated with a company
	if not request.user.companyapfytmanager:
		raise Http404

	print request.user.companyapfytmanager.company


	# context is the data that gets passed to the html template
	# we should gather data here and then add it to the template
	context = {
		"company": request.user.companyapfytmanager.company,
	}

	return render(request,'companies/company_profile.html', context)

# return render(request, 'contact.html', {
# 		'form': form,
#     })

class DealOfTheDayListView(ListView):
	model= DealOfTheDay

	def get(self, request, *args, **kwargs):
		# verifies that the user is associated with a company
		# maybe we should develope a company login
		# i don't like the idea of just raising and http 404 error 
		# i think it should redirect them to a login
		try:
			request.user.companyapfytmanager
		except:
			raise Http404

		return super(DealOfTheDayListView, self).get(request, *args, **kwargs)
	
	def get_queryset(self):
		return super(DealOfTheDayListView, self).get_queryset().filter(company=self.request.user.companyapfytmanager.company)

