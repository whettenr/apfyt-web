from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView

from .forms import GetSurveyForm
from .models import Answer, Question, Survey, SurveyResponse



# this is a form to take in a code form the user
# it sets a session variable that will be used to 
# access the survey and generate a survey response

class SurveyFormView(FormView):
 	template_name = "surveys/survey_response.html"
	form_class = GetSurveyForm
	success_url = "take_survey"

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():

			survey_code = form.cleaned_data.get("survey_code")
			
			try:
				survey = Survey.objects.get(id=survey_code)
			except:
				survey = None
				messages.error(self.request, "No survey could be found")

			if survey != None:
				request.session["survey_id"] = survey.id

			return self.form_valid(form)
		else:
			return self.form_invalid(form)

#survey response form
class AnswerCreateView(CreateView):
	model = Answer
	fields = '__all__'

		


