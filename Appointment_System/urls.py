"""
URL configuration for Appointment_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Home, Register, Login, logoutuser, Aboutus, Services, Contactus, Doctordetails,Doctor_information, Patientdetails, Priscription, profile_view, create_profile_view, Appointment_System,appointment_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name="homepage"),
    path('', Register, name="register"),
    path('loginpage', Login, name='loginpage'),
    path('logout/', logoutuser, name='logout'),
    path('aboutus/',Aboutus, name='aboutus'),
    path('services/', Services, name='services'),
    path('contactus', Contactus, name='contactus'),
    path('patient/', Patientdetails, name='patient'),
    path('doctor/', Doctordetails, name="doctor"),
    
    path('priscription/', Priscription, name='priscription'),
    path('profile/', profile_view, name='profile'),
    path('create_profile/', create_profile_view, name='create_profile'),
    path('appointment1/', Appointment_System, name='appointment1'),
    path('appointment_list/', appointment_list, name='appointment_list'),
    path('doctor_information/', Doctor_information, name='doctor_information'),

]

    

