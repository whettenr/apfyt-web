from rest_framework import serializers
from .models import Answer, Question, Survey, SurveyResponse
from companies.models import Company

from image_cropping.utils import get_backend



class CompanySerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_profile_image(self, obj):
        thumbnail_url = get_backend().get_thumbnail_url(
        obj.profile_image,
            {
                'size': (430, 360),
                'box': obj.cropping,
                'crop': True,
                'detail': True,
            }
        )
        print thumbnail_url
        return thumbnail_url

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    company = CompanySerializer()
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = '__all__'




