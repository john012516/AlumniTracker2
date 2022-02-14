from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import EventFilter

# Create your views here.

def homepage(request):
	#return HttpResponse("landing");
	return render(request, 'CITAT/landingpage.html')



def aboutpage(request):
	#return HttpResponse("Aboutus");
	return render(request, 'CITAT/about.html')


def useremployed(request):

	return render(request, 'CITAT/User_Employed.html')

def userunemployed(request):

	return render(request, 'CITAT/User_Unemployed.html')

def userselfemployed(request):

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


def dashboardpage(request):
	jobs = Jobs.objects.all()
	alumni = Alumni.objects.all()

	total_jobs = jobs.count()
	partnercompany = jobs.filter(status='Partner Company').count()
	jobseekers = jobs.filter(status='Job Seekers').count()

	context = {'jobs':jobs, 'alumni':alumni, 'total_jobs':total_jobs, 'partnercompany':partnercompany, 'jobseekers': jobseekers}

	return render(request, 'CITAT/dashboard.html', context)


def alumnipage(request, pk):
	alumni = Alumni.objects.get(id=pk)

	events = alumni.joinevent_set.all()

	context = {'alumni':alumni, 'events':events}
	return render(request, 'CITAT/Alumniprofile.html', context)

def eventpage(request):
	event = Event.objects.all()

	myFilter = EventFilter(request.GET, queryset=event)
	event = myFilter.qs

	ongoingevent = event.filter(status='On-Going Events').count()
	upcomingevent = event.filter(status='Upcoming Events').count()
	completeevent = event.filter(status='Completed Events').count()

	context = {'event':event, 'ongoingevent': ongoingevent, 'upcomingevent': upcomingevent, 'completeevent':completeevent,'myFilter':myFilter} 

	return render(request, 'CITAT/Events.html', context)

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

def deleteEvent(request, pk):
	event = Event.objects.get(id=pk)

	if request.method == "POST":
		 event.delete()
		 return redirect('event')

	context={'item':event}
	return render(request, 'CITAT/deleteevent.html', context)


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

def deleteJob(request, pk):
	jobs = Jobs.objects.get(id=pk)
	if request.method == "POST":
		 jobs.delete()
		 return redirect('dashboard')

	context={'item':jobs}
	return render(request, 'CITAT/deletejob.html', context)



