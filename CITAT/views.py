from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import EventFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import  UserEmployed, UserUnemployed, UserSelfemployed
# Create your views here.


@unauthenticated_user
def registerpage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('first_name')


			messages.success(request, 'Account was created for ' + username)
			return redirect('loginpage')

	
	context={'form': form}
	return render(request, 'CITAT/User_Register.html',context)

@unauthenticated_user
def loginpage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'username OR password is incorrect')


		# if request.method == 'POST':  
	context={}
	return render(request, 'CITAT/login.html',context )

def logoutUser(request):
	logout(request)
	return redirect('loginpage')

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['alumni'])
def userPage(request):
	jobs = Jobs.objects.all()

	total_jobs = jobs.count()
	partnercompany = jobs.filter(status='Partner Company').count()
	jobseekers = jobs.filter(status='Job Seekers').count()
	
	context = {'jobs':jobs,'total_jobs':total_jobs, 'partnercompany':partnercompany, 'jobseekers': jobseekers}
	return render(request, 'CITAT/user.html', context )


@login_required(login_url='loginpage')
@admin_only
def homepage(request):
	#return HttpResponse("landing");
	return render(request, 'CITAT/landingpage.html')


@login_required(login_url='loginpage')
def aboutpage(request):
	#return HttpResponse("Aboutus");
	return render(request, 'CITAT/about.html')

@login_required(login_url='loginpage')
def useremployed(request):

	return render(request, 'CITAT/User_Employed.html')



def add_useremployed_form_submission(request):

	print("Hello, Employed form is submitted.")
	employed = request.POST["employed"]
	organization = request.POST["organization"]
	selections = request.POST["selections"]
	income = request.POST["income"]
	skills = request.POST["skills"]

	user_employed = UserEmployed(employed=employed,organization=organization,selections=selections,income=income,skills=skills)
	user_employed.save()

	return render(request, 'CITAT/User_Employed.html')



@login_required(login_url='loginpage')
def userunemployed(request):

	return render(request, 'CITAT/User_Unemployed.html')



def add_userunemployed_form_submission(request, pk):
	alumni = Alumni.objects.get(id=pk)


	print("Hello, Unemployed form is submitted.")
	reasons = request.POST["reasons"]
	seek = request.POST["seek"]
	aftergrad = request.POST["aftergrad"]
	finance = request.POST["finance"]
	desire =  request.POST["desire"]
	consider = request.POST["consider"]

	user_unemployed = UserUnemployed(reasons=reasons,seek=seek,aftergrad=aftergrad,finance=finance,desire=desire,consider=consider)
	user_unemployed.save()

	context = {'alumni':alumni}

	return render(request, 'CITAT/User_Unemployed.html', context)	



@login_required(login_url='loginpage')
def userselfemployed(request):

	return render(request, 'CITAT/User_SelfEmployed.html')




def add_userselfemployed_form_submission(request):
	print("Hello, Self-employed form is submitted.") 
	business = request.POST["business"]
	#related_yes = request.POST["related_yes"]
	#related_no = request.POST["related_no"]
	related = request.POST["related"]
	reason = request.POST["reason"]
	numberofemployee = request.POST["numberofemployee"]
	skills = request.POST["skills"]

	user_selfemployed = UserSelfemployed(business=business,related=related,reason=reason,numberofemployee=numberofemployee,skills=skills)
	user_selfemployed.save()

	return render(request, 'CITAT/User_SelfEmployed.html')	




def contactpage(request):
	#return HttpResponse("contact");
	if request.method == "POST":
		contact = Contact()
		fname=request.POST.get('firstname')
		lname=request.POST.get('lastname')
		email=request.POST.get('Email')
		subject=request.POST.get('subject')

		contact.firstname=fname
		contact.lastname=lname
		contact.email=email
		contact.subject=subject

		contact.save()
		return HttpResponse("<h1> Thank you for contacting us!</h1>")
	return render(request, 'CITAT/contact.html')

@login_required(login_url='loginpage')
@admin_only
# @allowed_users(allowed_roles=['admin'])
def dashboardpage(request):
	jobs = Jobs.objects.all()
	alumni = Alumni.objects.all()

	total_jobs = jobs.count()
	partnercompany = jobs.filter(status='Partner Company').count()
	jobseekers = jobs.filter(status='Job Seekers').count()

	context = {'jobs':jobs, 'alumni':alumni, 'total_jobs':total_jobs, 'partnercompany':partnercompany, 'jobseekers': jobseekers}

	return render(request, 'CITAT/dashboard.html', context)


	

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def alumnipage(request, pk):
	alumni = Alumni.objects.get(id=pk)

	
	context = {'alumni':alumni}
	return render(request, 'CITAT/Alumniprofile.html', context)





@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def eventpage(request):
	event = Event.objects.all()

	myFilter = EventFilter(request.GET, queryset=event)
	event = myFilter.qs

	ongoingevent = event.filter(status='On-Going Events').count()
	upcomingevent = event.filter(status='Upcoming Events').count()
	completeevent = event.filter(status='Completed Events').count()

	context = {'event':event, 'ongoingevent': ongoingevent, 'upcomingevent': upcomingevent, 'completeevent':completeevent,'myFilter':myFilter} 

	return render(request, 'CITAT/Events.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def createEvent(request):
	form = EventForm()

	if request.method == "POST":
		#print(request.POST)
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('event')
	
	context = {'form': form}
	return render(request, 'CITAT/CRUDevent.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request, pk):
	event = Event.objects.get(id=pk)

	form = EventForm(instance=event)

	if request.method == "POST":
		form = EventForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			return redirect('event')

	context = {'form': form}

	return render(request, 'CITAT/CRUDevent.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, pk):
	event = Event.objects.get(id=pk)

	if request.method == "POST":
		 event.delete()
		 return redirect('event')

	context={'item':event}
	return render(request, 'CITAT/deleteevent.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def createJob(request):
	form = JobsForm()

	if request.method == "POST":
		#print(request.POST)
		form = JobsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard')



	context = {'form': form}
	return render(request, 'CITAT/CRUDjob.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateJob(request, pk):

	jobs = Jobs.objects.get(id=pk)
	form = JobsForm(instance=jobs)

	if request.method == "POST":
		form = JobsForm(request.POST, instance=jobs)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form': form}

	return render(request, 'CITAT/CRUDjob.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteJob(request, pk):
	jobs = Jobs.objects.get(id=pk)
	if request.method == "POST":
		 jobs.delete()
		 return redirect('dashboard')

	context={'item':jobs}
	return render(request, 'CITAT/deletejob.html', context)


@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['alumni'])
def accountSettings(request):
	alumni = request.user.alumni
	form = AlumniForm(instance=alumni)

	if request.method == "POST":
		form = AlumniForm(request.POST, request.FILES, instance=alumni)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'CITAT/account_settings.html', context)

def updateprofile(request):

	context={}

	return render (request,'CITAT/updateprofile.html')

