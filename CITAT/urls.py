from django.urls import path
from . import views
from django.contrib import admin






urlpatterns = [
    

    path('', views.homepage, name='home'),
    path('aboutus/', views.aboutpage, name='about'),
    path('contactus/', views.contactpage, name='contact'),
    path('dashboards/', views.dashboardpage, name='dashboard'),
    path('alumnidashboard/<str:pk>/', views.alumnipage, name="alumni"),
    path('eventdashboard/', views.eventpage, name='event'),

    path('create_job/', views.createJob, name='create_job'),
    path('update_job/<str:pk>/', views.updateJob, name='update_job'),
    path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),

    path('create_event/', views.createEvent, name='create_event'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),




]
