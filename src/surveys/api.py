from .models import Answer, Question, Survey, SurveyResponse
from .serializers import AnswerSerializer, QuestionSerializer, SurveySerializer, SurveyResponseSerializer

from rest_framework.viewsets import ModelViewSet

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
    queryset = Survey.objects.all()
    serializer_class = SurveyResponseSerializer
