from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from companies.models import Company
from users.models import CompanyApfytManager 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Survey(models.Model):
	company = models.ForeignKey(Company)
	# survey_author = models.ForeignKey(CompanyApfytManager)
	name = models.CharField(max_length=25)
	reward = models.TextField(max_length=500, null=True, blank=True)


	def __unicode__(self): #def __str__(self):
		return self.name


STYLE_CHOICES = (
	('rate', 'Rating'),
	('text', 'Text Response'),
	('mc', 'Multiple Choice'),
)

class MultipleChoiceOption(models.Model):
	text = models.CharField(max_length=140)

	def __unicode__(self): #def __str__(self):
		return str(self.text)


class Question(models.Model):
	survey	 = models.ForeignKey(Survey, related_name="questions")
	question = models.TextField(max_length=500)
	style = models.CharField(max_length=25, choices=STYLE_CHOICES, null=True, blank=True)
	required = models.BooleanField(default=True)
	choices = models.ManyToManyField(MultipleChoiceOption, blank=True)

	order = models.PositiveIntegerField(default=0)

	def __unicode__(self): #def __str__(self):
		return str(self.survey) + ", question " + str(self.order) 

	class Meta:
		unique_together = ('survey', 'question')
        ordering = ('order',)

RATE_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
)


class SurveyResponse(models.Model):
	apfyt_user = models.ForeignKey(settings.AUTH_USER_MODEL)
	survey = models.ForeignKey(Survey)
	completed = models.BooleanField(default=False)
	
	# records time when an instance is created
	start_time = models.DateField(auto_now_add=True)
	# record time when an instance is created
	last_edited = models.DateField(auto_now=True)
	
	def __unicode__(self): #def __str__(self):
		return "Response: " + str(self.survey)

	# returns percent value of completion
	# i.e.) 100 = complete 
	# 0 = no questions answered
	# 50 = half of questions answered
	def get_completion_status(self): 
		number_of_questions = self.survey.question_set.count()
		# print number_of_questions
		number_of_answers = self.answer_set.count()
		# print number_of_answers
		return number_of_answers/number_of_questions




class Answer(models.Model):
	question = models.ForeignKey(Question)
	survey_response = models.ForeignKey(SurveyResponse)
	response_text = models.TextField(max_length=500, null=True, blank=True)
	response_rate = models.PositiveIntegerField(
		choices=RATE_CHOICES, 
		validators=[MinValueValidator(1), MaxValueValidator(10)], 
		null=True, 
		blank=True)
	response_multiple_choice_selected = models.ForeignKey(MultipleChoiceOption, null=True, blank=True)

	# records time when an instance is created
	created_on = models.DateField(auto_now_add=True)
	# records time when an instance is edited
	last_edited_on = models.DateField(auto_now=True)

	def __unicode__(self): #def __str__(self):
		return "Answer: " + str(self.question) 


