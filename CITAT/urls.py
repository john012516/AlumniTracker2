from django.urls import path
from . import views
from django.contrib import admin






urlpatterns = [
    path('login', views.loginpage, name='loginpage'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerpage, name='registerpage'),

    path('', views.homepage, name='home'),
    path('user', views.userPage, name='userPage'),
    path('aboutus/', views.aboutpage, name='about'),
    path('contactus/', views.contactpage, name='contact'),
    path('dashboards/', views.dashboardpage, name='dashboard'),
    path('alumnidashboard/<str:pk>/', views.alumnipage, name="alumni"),
    path('eventdashboard/', views.eventpage, name='event'),
    path('useremployed/', views.useremployed, name="useremployed"),
    path('userunemployed/', views.userunemployed, name="userunemployed"),
    path('userselfemployed/', views.userselfemployed, name="userselfemployed"),

    path('create_job/', views.createJob, name='create_job'),
    path('update_job/<str:pk>/', views.updateJob, name='update_job'),
    path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),

    path('create_event/', views.createEvent, name='create_event'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),




]
