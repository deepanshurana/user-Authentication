from django.urls import path
from basicApp import views

urlpatterns = [

    path('/registration', views.registerationPage, name='registerationPage' ),
    path('/login', views.loginPage, name='loginPage'),
]
