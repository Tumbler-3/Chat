from django import forms


class CreateMessage(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
                           'type': 'text', 'class': 'form-control', 'placeholder': 'Type your message'}), label=False)
    photo = forms.ImageField(required=False, label=False)
