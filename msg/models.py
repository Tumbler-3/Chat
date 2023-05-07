from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    text = models.TextField(null=False)
    photo = models.ImageField(null=True, blank=True, upload_to='media')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)