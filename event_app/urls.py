"""woc_eventmanager_Rutuba_Chudasama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from event_app import views
from django.urls import path

urlpatterns = [
    path('', views.index , name='index'),
    path('index', views.index , name='index'),
    path('Event_Registration' , views.registration , name='Event Registration'),
    path('Submit_Registration' , views.registration_sub),
    path('Participant' , views.participant , name='Participant'),
    path('Participant_Registration' , views.participant_registration, name='Participant Registration'),
    path('Submit_Participant' , views.Participant_sub),
    path('Event_Dashboard' , views.dashboard , name ='Event_Dashboard')
]
