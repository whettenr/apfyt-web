from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    contact_company = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Company'}))
    contact_subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name "
        self.fields['contact_email'].label = "Email"
        self.fields['contact_company'].label = "Company"
        self.fields['contact_subject'].label = "Subject"
        self.fields['content'].label = "A Penny For Your Thoughts"