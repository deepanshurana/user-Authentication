from django.shortcuts import render

# Create your views here.
from basicApp import forms

# login imports
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'basicApp/index.html')


def registrationPage(request):
    isRegistered = False
    if request.method == 'POST':
        userFormObj = forms.userForm(data=request.POST)
        profileFormObj = forms.userProfileInfoForm(data=request.POST)

        if userFormObj.is_valid() and profileFormObj.is_valid():
            user = userFormObj.save()
            user.set_password(user.password)
            user.save()
            profile = profileFormObj.save(commit=False)
            profile.user = user
            if 'profilePic' in request.FILES:
                print('Profile Picture Found.')
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            isRegistered = True
        else:
            print(userFormObj.errors, profileFormObj.errors)
    else:
        userFormObj = forms.userForm()
        profileFormObj = forms.userProfileInfoForm()
    formDict = {'userForm': userFormObj, 'profileForm': profileFormObj,
                'isRegistered': isRegistered}
    return render(request, 'basicApp/registration.html', context=formDict)


def loginPage(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        # using django built-in authentication function.
        user = authenticate(username=userName, password=passWord)
        if user:
            if user.is_active:
                login(request, user) # login function.
                return HttpResponseRedirect(reverse(index))
            # redirect to home page.
            else:
                # print some statement.
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print("USERNAME:",userName, "PASSWORD: ", passWord)
            return HttpResponse('INVALID LOGIN DETAILS PROVIDED.')

    else:
        return render(request, 'basicApp/login.html', {})

@login_required
def logOutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are Loggedin. NICE!!!")
