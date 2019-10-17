from django.contrib import admin
from django.urls import path, include
from basicApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basicApp/', include(('basicApp.urls', 'basicApp'),
                              namespace='basicApp')),
    path('logout/', views.logOutPage, name='logout'),
    path('special/', views.special, name='special'),
]
