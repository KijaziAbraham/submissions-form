from django.contrib import admin
from .models import UserSubmission

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'dob', 'gender', 'email',
        'mobile_number', 'mailing_address', 'country', 
    )
    search_fields = ('first_name', 'last_name', 'email', 'mobile_number')
    list_filter = ('gender',)
    readonly_fields = ('resume', 'identification_document')

    def has_add_permission(self, request):
        # Disable the ability to add new entries directly from the admin interface
        return False
