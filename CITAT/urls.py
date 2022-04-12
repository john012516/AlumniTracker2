from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin






urlpatterns = [
    path('login', views.loginpage, name='loginpage'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerpage, name='registerpage'),

    path('', views.homepage, name='home'),
    path('navbar', views.navbar, name='navbar'),
    path('user', views.userPage, name='userPage'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('aboutus/', views.aboutpage, name='about'),
    path('contactus/', views.contactpage, name='contact'),
    path('dashboards/', views.dashboardpage, name='dashboard'),
    path('alumnidashboard/<str:pk>/', views.alumnipage, name="alumni"),
    path('jobdashboard/', views.jobpage, name='jobpage'),
    path('eventdashboard/', views.eventpage, name='event'),
    path('eventsAlumni/', views.eventsAlumni, name='eventsAlumni'),
    path('countrylist/', views.countrylist, name='countrylist'),

    path('account/', views.accountSettings, name='account'),

    path('genderstatus/', views.genderstatus, name='genderstatus'),
    path('coursestatus/', views.coursestatus, name='coursestatus'),
    path('employedstatus/', views.employedstatus, name='employedstatus'),
    path('countrystatus/', views.countrystatus, name='countrystatus'),
    path('Home/', views.Home, name='Home'),

    path('employed/', views.employed, name="employed"),

    path('addcompany/', views.addcompany, name='addcompany'),
    path('companygallery/', views.companygallery, name='companygallery'),
    path('viewcompany/<str:pk>/', views.viewcompany, name='viewcompany'),
    path('jobsView/<str:pk>/', views.jobsView, name='jobsView'),
    path('AdminjobsView/<str:pk>/', views.AdminjobsView, name='AdminjobsView'),
    path('EventView/<str:pk>/', views.EventView, name='EventView'),
    path('AdminEventView/<str:pk>/', views.AdminEventView, name='AdminEventView'),



    # path('useremployed/', views.useremployed, name="useremployed"),
    # path('add_useremployed_form_submission/', views.add_useremployed_form_submission, name="add_useremployed_form_submission"),
    # path('userunemployed/', views.userunemployed, name="userunemployed"),
    # path('add_userunemployed_form_submission/', views.add_userunemployed_form_submission, name="add_userunemployed_form_submission"),
    # path('userselfemployed/', views.userselfemployed, name="userselfemployed"),
    # path('add_userselfemployed_form_submission/', views.add_userselfemployed_form_submission, name="add_userselfemployed_form_submission"),

    path('create_job/', views.createJob, name='create_job'),
    path('update_job/<str:pk>/', views.updateJob, name='update_job'),
    path('delete_job/<str:pk>/', views.deleteJob, name='delete_job'),

    path('create_event/', views.createEvent, name='create_event'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="CITAT/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="CITAT/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="CITAT/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="CITAT/password_reset_done.html"), name="password_reset_complete"),






]
