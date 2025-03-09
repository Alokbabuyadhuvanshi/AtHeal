from django.db import models
from Healio.models import User
from Patient.models import Patient

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/')
    Specialization = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Experience =  models.PositiveIntegerField(default=0, blank=True, null=True)
    Contact = models.CharField(max_length=10)
    Address = models.TextField()

    def __str__(self):
        return f"{self.user.username}"
