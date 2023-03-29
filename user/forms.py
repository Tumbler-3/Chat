from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Create username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Create password'}))
    confirm__password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password'}))