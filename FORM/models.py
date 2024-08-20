from django.db import models
from django_countries.fields import CountryField

class UserSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    mailing_address = models.CharField(max_length=255)
    country = CountryField()  # Updated to use CountryField
    resume = models.FileField(upload_to='resumes/')
    identification_document = models.FileField(upload_to='identification_documents/')

def __str__(self):
        return f"{self.first_name} {self.last_name}"