from django import forms

class ContactForm(forms.Form):
    contact_firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First', 'class': 'form-control'}))
    contact_lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last', 'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    contact_company = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}))
    contact_subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))
    
    # contact_firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First', 'class': 'form-control-two'}))
    # contact_lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last', 'class': 'form-control-two'}))
    # contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control-two'}))
    # contact_company = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control-two'}))
    # contact_subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    # content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # self.fields['contact_firstname'].label = "Name "
        # self.fields['contact_lastname'].label = ""
        # self.fields['contact_email'].label = "Email"
        # self.fields['contact_company'].label = "Company"
        # self.fields['contact_subject'].label = "Subject"
        # self.fields['content'].label = "A Penny For Your Thoughts"