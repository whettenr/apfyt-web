from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from surveys.models import Answer, MultipleChoiceOption, Question, Survey, SurveyResponse
from companies.models import DealOfTheDay
from .serializers import AnswerSerializer, MultipleChoiceOptionSerializer, QuestionSerializer, SurveySerializer, SurveyResponseSerializer
from rest_framework.viewsets import ModelViewSet



# serializers facebook login

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


# serializers for models in surveys.models

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class SurveyResponseViewSet(ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

class MultipleChoiceOptionViewSet(ModelViewSet):
	queryset = MultipleChoiceOption.objects.all()
	serializer_class = MultipleChoiceOptionSerializer

# serializers for models in companies.models

# class DealOfTheDay():

