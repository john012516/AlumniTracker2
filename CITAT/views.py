from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.

def homepage(request):
	#return HttpResponse("landing");
	return render(request, 'CITAT/landingpage.html')



def aboutpage(request):
	#return HttpResponse("Aboutus");
	return render(request, 'CITAT/about.html')



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
		return HttpResponse("<h1> Thankyou for Contactin Us</h1>")
	return render(request, 'CITAT/contact.html')


def dashboardpage(request):
	return render(request, 'CITAT/dashboard.html')


def alumnipage(request):
	return render(request, 'CITAT/Alumni.html')

def eventpage(request):
	return render(request, 'CITAT/Events.html')