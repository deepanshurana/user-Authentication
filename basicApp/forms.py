from django import forms
from basicApp.models import userProfileInfo
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class userProfileInfoForm(forms.ModelForm):
    class Meta:
        model = userProfileInfo
        fields = ('portfolio', 'profilePic')
        
