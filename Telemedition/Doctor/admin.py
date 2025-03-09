from django.contrib import admin
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ['user', 'Specialization', 'Qualification', 'Experience', 'Contact', 'Address']
    search_fields = ['name__username', 'Specialization']

admin.site.register(Doctor, DoctorAdmin)