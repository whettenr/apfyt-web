from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .api import (
	AnswerViewSet, 
	QuestionViewSet,
	SurveyViewSet,
	SurveyResponseViewSet)

from .views import (
	SurveyFormView,
	AnswerCreateView,
	)

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="surveys/survey_home.html")),
	url(r'^response/set/$', SurveyFormView.as_view(), name='set_survey'),

	# this pk value is the value of the question being answered
    url(r'response/(?P<pk>\d+)/$', AnswerCreateView.as_view(), name='answer_view'),
	
	# url(r'^all/$', SurveyList.as_view(), name='set_survey')
]


router = DefaultRouter()

router.register(r'answers_api', AnswerViewSet)
router.register(r'questions_api', QuestionViewSet)
router.register(r'surveys_api', SurveyViewSet)
router.register(r'survey_responses_api', SurveyResponseViewSet)

urlpatterns += router.urls