from django.db import models
from django.contrib.auth.models import User


class GroupChat(models.Model):
    groupname = models.CharField(max_length=200)
    participants = models.ManyToManyField(User)


class GroupChatMessage(models.Model):
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(null=False)
    photo = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
