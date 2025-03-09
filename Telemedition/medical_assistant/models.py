from django.db import models
from Healio.models import User
# Create your models here.

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100)
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} conversation"
    
class Message(models.Model):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('assistant', 'Assistant'),
        )
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} : {self.content[:50]}..."
    


