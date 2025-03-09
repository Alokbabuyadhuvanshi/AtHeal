from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['user', 'Age', 'problems', 'Contact', 'Address']
    search_fields = ['name_username', 'problems']

admin.site.register(Patient, PatientAdmin)