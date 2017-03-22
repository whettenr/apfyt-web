from django import forms

class GetSurveyForm(forms.Form):
    survey_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Code', 'class': 'form-control'}))
    
#class GetSurveyForm(forms.Form):
#    survey_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Code', 'class': 'form-control'}))
    
class GetAnswerForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))
    
 