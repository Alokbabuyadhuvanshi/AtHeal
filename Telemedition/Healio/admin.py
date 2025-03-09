from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User
from Doctor.models import Doctor
from Patient.models import Patient

# Inline for Doctor Details
class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    readonly_fields = ('Specialization', 'Qualification', 'Experience', 'Contact', 'Address')
    extra = 0  # No extra empty forms

# Inline for Patient Details
class PatientInline(admin.StackedInline):
    model = Patient
    can_delete = False
    readonly_fields = ('Age', 'problems', 'Contact', 'Address')
    extra = 0

# Custom UserAdmin to include Doctor and Patient details
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_doctor', 'is_patient','is_staff']
    list_filter = ['is_doctor', 'is_patient', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    inlines = []  # We will add inlines conditionally

    def get_inlines(self, request, obj=None):
        if obj:
            if obj.is_doctor:
                return [DoctorInline]
            elif obj.is_patient:
                return [PatientInline]
        return []

# Registering Admin Models
admin.site.register(User, CustomUserAdmin)


