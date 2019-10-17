from django.urls import path
from basicApp import views

app_name = 'basicApp'
urlpatterns = [

    path('registration/', views.registrationPage, name='registration'),
    path('login/', views.loginPage, name='login'),
]
