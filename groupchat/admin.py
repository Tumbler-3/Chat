from django.contrib import admin
from groupchat.models import GroupChat, GroupChatMessage


admin.site.register(GroupChatMessage)
admin.site.register(GroupChat)