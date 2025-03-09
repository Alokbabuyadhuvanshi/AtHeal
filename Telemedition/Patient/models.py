from django.db import models
from Healio.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient/')
    Age =models.PositiveIntegerField(default=0, blank=True, null=True)
    problems = models.TextField(blank=True)
    Contact = models.CharField(max_length=10)
    Address = models.TextField()

    def __str__(self):
        return f"{self.user.username}"