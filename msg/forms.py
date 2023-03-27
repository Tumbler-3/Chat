from django import forms

class CreateMessage(forms.Form):
    text = forms.CharField()
    photo = forms.ImageField(required=False)