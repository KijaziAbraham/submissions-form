from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import UserSubmissionForm
from django.template.loader import render_to_string

def submit_form(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            # Prepare URLs for the uploaded files
            resume_url = request.build_absolute_uri(submission.resume.url)
            identification_document_url = request.build_absolute_uri(submission.identification_document.url)
            
            # Send email to manager
            manager_email_subject = 'New Submission Received'
            manager_email_message = render_to_string('manager_email.html', {
                'first_name': submission.first_name,
                'middle_name': submission.middle_name,
                'last_name': submission.last_name,
                'dob': submission.dob,
                'gender': submission.gender,
                'email': submission.email,
                'mobile_number': submission.mobile_number,
                'mailing_address': submission.mailing_address,
                'country': submission.country,
                'resume_url': resume_url,
                'identification_document_url': identification_document_url,
            })
            send_mail(
                manager_email_subject,
                manager_email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['abrahamkijazi01@gmail.com'],
                fail_silently=False,
                html_message=manager_email_message
            )
            
            # Send confirmation email to user
            user_email_subject = 'Submission Received'
            user_email_message = render_to_string('user_confirmation_email.html', {
                'first_name': submission.first_name,
            })
            send_mail(
                user_email_subject,
                user_email_message,
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
                fail_silently=False,
                html_message=user_email_message
            )
            return redirect('success')
        else:
            # Render the form again with validation errors
            return render(request, 'form.html', {'form': form})
    else:
        form = UserSubmissionForm()
    return render(request, 'form.html', {'form': form})


def success(request):
    return render(request, 'success.html')
