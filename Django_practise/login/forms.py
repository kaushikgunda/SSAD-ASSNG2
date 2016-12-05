from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'SignUp with email address already exists.')
        return email

    def clean_username(self):
        form_username = self.cleaned_data.get('username')
        if User.objects.filter(username = form_username).exists():
            raise forms.ValidationError(u'username already exists choose another one.')
        return form_username

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()