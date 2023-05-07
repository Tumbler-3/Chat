from django import forms
from django.contrib.auth.models import User



class GroupChatForm(forms.Form):
    groupname = forms.CharField()
    participants = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=None)
    
    def __init__(self, user=None, *args, **kwargs):
        super(GroupChatForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['participants'].queryset = User.objects.exclude(id=user.id)
        else:
            self.fields['participants'].queryset = User.objects.all()
        


class GroupChatMessageForm(forms.Form):
    text = forms.CharField(label=False)
    photo = forms.ImageField(label=False, required=False)
    