from rest_framework import serializers
from companies.models import Company
from surveys.models import Answer, MultipleChoiceOption, Question, Survey, SurveyResponse
from users.models import ApfytUser

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

class ApfytUserSerializer(serializers.ModelSerializer):
    class meta:
        model = ApfytUser
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class MultipleChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceOption
        fields = '__all__'
        
class QuestionSerializer(serializers.ModelSerializer):
    choices = MultipleChoiceOptionSerializer(many=True)

    def create(self):
        print self

    class Meta:
        model = Question
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True,read_only=True)

    # company = CompanySerializer()
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = '__all__'




