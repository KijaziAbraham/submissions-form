from django import forms
from .models import UserSubmission
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from django_countries.widgets import CountrySelectWidget


class UserSubmissionForm(forms.ModelForm):
    mobile_number = forms.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        max_length=20
    )
    resume = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    identification_document = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])]
    )
    
    class Meta:
        model = UserSubmission
        fields = [
            'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'email',
            'mobile_number', 'mailing_address', 'country', 
            'resume', 'identification_document'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female')]),
            'country': CountrySelectWidget(attrs={'class': 'form-control', 'placeholder': 'Select your country'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'identification_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].empty_label = "Select your country"
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserSubmission.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email
