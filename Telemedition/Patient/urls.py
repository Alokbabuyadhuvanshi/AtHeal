from django.urls import path
from .views import update_password, Update_patient_info

urlpatterns = [
    path('update_password/', update_password, name='update_password'),
    path('update_patient_info/', Update_patient_info, name='update_patient_info'),
]

