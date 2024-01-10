from django.contrib import admin
from service.models import Contact, Patient, Doctor
from django.contrib.auth.admin import UserAdmin
from .models import Apps

def approve_apps(modeladmin, request, queryset):
    queryset.update(is_approved=True)

approve_apps.short_description = "Approve selected apps"

class AppAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'phoneNo', 'is_approved']

    def save_model(self, request, obj, form, change):
        # Check if the is_approved checkbox is checked in the admin form
        is_approved = form.cleaned_data.get('is_approved')

        if is_approved:
            obj.is_approved = True
            obj.save()
        else:
            # If not approved, you might want to take some other action or not save at all
            # For example, you can redirect the user to a rejection page or raise an exception
            pass

admin.site.register(Apps, AppAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display=('fname', 'lname', 'gender', 'date_of_birth','aadharnumber','email','phonenumber','bloodgroup',
           'address', 'symptoms','ename','relation', 'emergencynumber')
admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=('dname', 'specialization', 'gender','email','phonenumber')
admin.site.register(Doctor, DoctorAdmin)