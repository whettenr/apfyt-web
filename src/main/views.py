from django.shortcuts import render

from django.conf import settings

from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from .forms import ContactForm

def contact(request):
	form = ContactForm
	if request.method == 'POST':
		form = form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			contact_company = request.POST.get('contact_company', '')
			contact_subject = request.POST.get('contact_subject', '') 
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'contact_company': contact_company,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				"Subject: " + contact_subject,
				content,
				settings.EMAIL_MAIN,
				['snare117@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			messages.success(request, 'Email sent!')
			return redirect('contact')

	return render(request, 'contact.html', {
		'form': form,
    })