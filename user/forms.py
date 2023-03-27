from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label=False)
    password = forms.CharField(label=False)