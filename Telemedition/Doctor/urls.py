from django.urls import path
from .views import consult_doctor, update_doctor_info, update_password

urlpatterns = [
    path('consult-doctor/', consult_doctor, name='consult_doctor'),
    path('update_password/', update_password, name='update_password'),
    path('update_dcotor_info/' , update_doctor_info, name='update_doctor_info'),
]
