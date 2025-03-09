from django.urls import path
from .import views
urlpatterns = [
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('update-appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('my-appointments/', views.patient_appointments, name='patient_appointments'),
    path("start_video_call/<int:appointment_id>/", views.start_video_call, name="start_video_call"),
    path('video_call/',views.video_call, name='video_call'),
    path('end_video_call/<int:appointment_id>/', views.end_video_call, name='end_video_call'),
]