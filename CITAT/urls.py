from django.urls import path
from . import views
from django.contrib import admin






urlpatterns = [
    

    path('', views.homepage, name='home'),
    path('aboutus/', views.aboutpage, name='about'),
    path('contactus/', views.contactpage, name='contact'),
    path('dashboards/', views.dashboardpage, name='dashboard'),
    path('alumnidashboard/', views.alumnipage, name='alumni'),
    path('eventdashboard/', views.eventpage, name='event'),


]
