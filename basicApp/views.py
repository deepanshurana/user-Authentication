from django.shortcuts import render

# Create your views here.
from basicApp.models import userProfileInfo, User
from basicApp import forms


def index(request):
    return render(request, 'basicApp/index.html')


def registrationPage(request):
    form = forms.userProfileInfoForm()
    formDict = {''}
    return render(request, 'basicApp/registration.html', context= )


def loginPage(request):
    return render(request, 'basicApp/login.html', context= )
