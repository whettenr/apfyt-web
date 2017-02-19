from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .api import (
	AnswerViewSet, 
	QuestionViewSet,
	SurveyViewSet,
	SurveyResponseViewSet)

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="surveys/survey_home.html")),
]


router = DefaultRouter()

router.register(r'answers_api', AnswerViewSet)
router.register(r'questions_api', QuestionViewSet)
router.register(r'surveys_api', SurveyViewSet)
router.register(r'survey_responses_api', SurveyResponseViewSet)

urlpatterns += router.urls