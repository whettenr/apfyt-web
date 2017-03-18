from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


from .api import (
	AnswerViewSet,
	FacebookLogin,
	MultipleChoiceOptionViewSet, 
	QuestionViewSet,
	SurveyViewSet,
	SurveyResponseViewSet)

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]


router = DefaultRouter()

router.register(r'answers', AnswerViewSet)
router.register(r'multiple_choice', MultipleChoiceOptionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', SurveyResponseViewSet, base_name='responses')
router.register(r'surveys', SurveyViewSet)

urlpatterns += router.urls