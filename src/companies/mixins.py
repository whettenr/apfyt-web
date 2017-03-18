from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator

# these mixins can be used with class based views to 
# check if a user is logging in or associated with a company
# before displaying a view

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request,*args, **kwargs)

class CompanyManagerStatusRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		try:
			request.user.companyapfytmanager
		except:
			raise Http404
		return super(CompanyManagerStatusRequiredMixin, self).dispatch(request,*args, **kwargs)