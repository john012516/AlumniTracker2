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
			messages.info(request, 'Username or Password is Incorrect')


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
def userunemployed(request):

	return render(request, 'CITAT/User_Unemployed.html')



# def add_userunemployed_form_submission(request):
	


# 	print("Hello, Unemployed form is submitted.")
# 	reasons = request.POST["reasons"]
# 	seek = request.POST["seek"]
# 	aftergrad = request.POST["aftergrad"]
# 	finance = request.POST["finance"]
# 	desire =  request.POST["desire"]
# 	consider = request.POST["consider"]

# 	user_unemployed = UserUnemployed(reasons=reasons,seek=seek,aftergrad=aftergrad,finance=finance,desire=desire,consider=consider)
# 	user_unemployed.save()

# 	context = {'alumni':alumni}

# 	return render(request, 'CITAT/User_Unemployed.html', context)	



# @login_required(login_url='loginpage')
# def userselfemployed(request):

# 	return render(request, 'CITAT/User_SelfEmployed.html')




# def add_userselfemployed_form_submission(request):
# 	print("Hello, Self-employed form is submitted.") 
# 	business = request.POST["business"]
# 	#related_yes = request.POST["related_yes"]
# 	#related_no = request.POST["related_no"]
# 	related = request.POST["related"]
# 	reason = request.POST["reason"]
# 	numberofemployee = request.POST["numberofemployee"]
# 	skills = request.POST["skills"]

# 	user_selfemployed = UserSelfemployed(business=business,related=related,reason=reason,numberofemployee=numberofemployee,skills=skills)
# 	user_selfemployed.save()

# 	return render(request, 'CITAT/User_SelfEmployed.html')	




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
	employed = Employed.objects.all()

	total_alumni = alumni.count()
	male = alumni.filter(Gender='MALE').count()
	female = alumni.filter(Gender='FEMALE').count()
	bsit = alumni.filter(Course="BSIT").count()
	bscs = alumni.filter(Course="BSCS").count()
	emp = alumni.filter(alumni_employed="Employed").count()
	unemp = alumni.filter(alumni_employed="Unemployed").count()
	selfemp = alumni.filter(alumni_employed="Self-employed").count()
	Afghanistan = alumni.filter(Country="Afghanistan").count()
	Albania = alumni.filter(Country="Albania").count()
	Algeria = alumni.filter(Country="Algeria").count()
	AmericanSamoa = alumni.filter(Country="American Samoa").count()
	Andorra = alumni.filter(Country="Andorra").count()
	Angola = alumni.filter(Country="Angola").count()
	Anguilla = alumni.filter(Country="Anguilla").count()
	AntiguaBarbuda = alumni.filter(Country="Antigua & Barbuda").count()
	Argentina = alumni.filter(Country="Argentina").count()
	Armenia = alumni.filter(Country="Armenia").count()
	Aruba = alumni.filter(Country="Aruba").count()
	Australia = alumni.filter(Country="Australia").count()
	Austria = alumni.filter(Country="Austria").count()
	Azerbaijan = alumni.filter(Country="Azerbaijan").count()
	Bahamas = alumni.filter(Country="Bahamas").count()
	Bahrain = alumni.filter(Country="Bahrain").count()
	Bangladesh = alumni.filter(Country="Bangladesh").count()
	Barbados = alumni.filter(Country="Barbados").count()
	Belarus = alumni.filter(Country="Belarus").count()
	Belgium = alumni.filter(Country="Belgium").count()
	Belize = alumni.filter(Country="Belize").count()
	Benin = alumni.filter(Country="Benin").count()
	Bermuda = alumni.filter(Country="Bermuda").count()
	Bhutan = alumni.filter(Country="Bhutan").count()
	Bolivia = alumni.filter(Country="Bolivia").count()
	Bonaire = alumni.filter(Country="Bonaire").count()
	BosniaHerzegovina = alumni.filter(Country="Bosnia & Herzegovina").count()
	Botswana = alumni.filter(Country="Botswana").count()
	Brazil = alumni.filter(Country="Brazil").count()
	BritishIndianOceanTer = alumni.filter(Country="British Indian Ocean Ter").count()
	Brunei = alumni.filter(Country="Brunei").count()
	Bulgaria = alumni.filter(Country="Bulgaria").count()
	Cambodia = alumni.filter(Country="Cambodia").count()
	Cameroon = alumni.filter(Country="Cameroon").count()
	Canada = alumni.filter(Country="Canada").count()
	CanaryIslands = alumni.filter(Country="Canary Islands").count()
	CapeVerde = alumni.filter(Country="Cape Verde").count()
	CaymanIslands = alumni.filter(Country="Cayman Islands").count()
	CentralAfricanRepublic = alumni.filter(Country="Central African Republic").count()
	Chad = alumni.filter(Country="Chad").count()
	ChannelIslands = alumni.filter(Country="Channel Islands").count()
	Chile = alumni.filter(Country="Chile").count()
	China = alumni.filter(Country="China").count()
	ChristmasIsland = alumni.filter(Country="Christmas Island").count()
	CocosIsland = alumni.filter(Country="Cocos Island").count()
	Colombia = alumni.filter(Country="Colombia").count()
	Comoros = alumni.filter(Country="Comoros").count()
	Congo = alumni.filter(Country="Congo").count()
	CookIslands = alumni.filter(Country="Cook Islands").count()
	CostaRica = alumni.filter(Country="Costa Rica").count()
	CoteDIvoire = alumni.filter(Country="Cote DIvoire").count()
	Croatia = alumni.filter(Country="Croatia").count()
	Cuba = alumni.filter(Country="Cuba").count()
	Curacao = alumni.filter(Country="Curacao").count()
	Cyprus = alumni.filter(Country="Cyprus").count()
	CzechRepublic = alumni.filter(Country="Czech Republic").count()
	Denmark = alumni.filter(Country="Denmark").count()
	Djibouti = alumni.filter(Country="Djibouti").count()
	Dominica = alumni.filter(Country="Dominica").count()
	DominicanRepublic = alumni.filter(Country="Dominican Republic").count()
	EastTimor = alumni.filter(Country="East Timor").count()
	Ecuador = alumni.filter(Country="Ecuador").count()
	Egypt = alumni.filter(Country="Egypt").count()
	ElSalvador = alumni.filter(Country="El Salvador").count()
	EquatorialGuinea = alumni.filter(Country="Equatorial Guinea").count()
	Eritrea = alumni.filter(Country="Eritrea").count()
	Estonia = alumni.filter(Country="Estonia").count()
	Ethiopia = alumni.filter(Country="Ethiopia").count()
	FalklandIslands = alumni.filter(Country="Falkland Islands").count()
	FaroeIslands = alumni.filter(Country="Faroe Islands").count()
	Fiji = alumni.filter(Country="Fiji").count()
	Finland = alumni.filter(Country="Finland").count()
	France = alumni.filter(Country="France").count()
	FrenchGuiana = alumni.filter(Country="French Guiana").count()
	FrenchPolynesia = alumni.filter(Country="French Polynesia").count()
	FrenchSouthernTer = alumni.filter(Country="French Southern Ter").count()
	Gabon = alumni.filter(Country="Gabon").count()
	Gambia = alumni.filter(Country="Gambia").count()
	Georgia = alumni.filter(Country="Georgia").count()
	Germany = alumni.filter(Country="Germany").count()
	Ghana = alumni.filter(Country="Ghana").count()
	Gibraltar = alumni.filter(Country="Gibraltar").count()
	GreatBritain = alumni.filter(Country="Great Britain").count()
	Greece = alumni.filter(Country="Greece").count()
	Greenland = alumni.filter(Country="Greenland").count()
	Grenada = alumni.filter(Country="Grenada").count()
	Guadeloupe = alumni.filter(Country="Guadeloupe").count()
	Guam = alumni.filter(Country="Guam").count()
	Guatemala = alumni.filter(Country="Guatemala").count()
	Guinea = alumni.filter(Country="Guinea").count()
	Guyana = alumni.filter(Country="Guyana").count()





    
	context = {'jobs':jobs, 'alumni':alumni, 'total_alumni':total_alumni, 'male':male, 'female': female, 
	'bsit': bsit, 'bscs': bscs, 'emp': emp, 'unemp': unemp, 'selfemp': selfemp, 'employed': employed, 

	'Afghanistan': Afghanistan, 'Albania': Albania,
	'Algeria': Algeria, 'AmericanSamoa': AmericanSamoa, 'Andorra': Andorra, 'Angola': Angola, 'Anguilla': Anguilla, 'AntiguaBarbuda': AntiguaBarbuda,
	'Argentina': Argentina, 'Armenia': Armenia, 'Aruba': Aruba, 'Australia': Australia, 'Austria': Austria, 'Azerbaijan': Azerbaijan, 

	'Bahamas': Bahamas, 'Bahrain': Bahrain, 'Bangladesh': Bangladesh, 'Barbados': Barbados, 'Belarus': Belarus, 'Belgium': Belgium, 'Belize': Belize, 'Benin': Benin, 'Bermuda': Bermuda,
	'Bhutan': Bhutan, 'Bolivia': Bolivia, 'Bonaire': Bonaire, 'BosniaHerzegovina': BosniaHerzegovina, 'Botswana': Botswana, 'Brazil': Brazil, 'BritishIndianOceanTer': BritishIndianOceanTer,
	'Brunei': Brunei, 'Bulgaria': Bulgaria,

	'Cambodia': Cambodia, 'Cameroon': Cameroon, 'Canada': Canada, 'CanaryIslands': CanaryIslands, 'CapeVerde' :CapeVerde, 'CaymanIslands': CaymanIslands, 'CentralAfricanRepublic': CentralAfricanRepublic,
	'Chad': Chad, 'ChannelIslands': ChannelIslands, 'Chile': Chile, 'China': China, 'ChristmasIsland': ChristmasIsland, 'CocosIsland': CocosIsland, 'Colombia': Colombia, 'Comoros': Comoros, 
	'Congo': Congo, 'CookIslands': CookIslands, 'CostaRica': CostaRica, 'CoteDIvoire': CoteDIvoire, 'Croatia': Croatia, 'Cuba': Cuba, 'Curacao': Curacao, 'Cyprus': Cyprus, 'CzechRepublic': CzechRepublic,

	'Denmark': Denmark, 'Djibouti': Djibouti, 'Dominica': Dominica, 'DominicanRepublic': DominicanRepublic, 'Gibraltar': Gibraltar, 

	'EastTimor': EastTimor, 'Ecuador': Ecuador, 'Egypt': Egypt, 'ElSalvador': ElSalvador, 'EquatorialGuinea': EquatorialGuinea, 'Eritrea': Eritrea, 'Estonia': Estonia, 'Ethiopia': Ethiopia,

	'FalklandIslands': FalklandIslands, 'FaroeIslands': FaroeIslands, 'Fiji': Fiji, 'Finland': Finland, 'France': France, 'FrenchGuiana': FrenchGuiana, 'FrenchPolynesia': FrenchPolynesia,
	'FrenchSouthernTer': FrenchSouthernTer,

	'Gabon': Gabon, 'Gambia': Gambia, 'Georgia': Georgia, 'Germany': Germany, 'Ghana': Ghana, 'GreatBritain': GreatBritain, 'Greece': Greece, 'Greenland': Greenland, 'Grenada': Grenada, 
	'Guadeloupe': Guadeloupe, 'Guam': Guam, 'Guatemala': Guatemala, 'Guinea': Guinea, 'Guyana': Guyana




	}

	return render(request, 'CITAT/dashboard.html', context)


@login_required(login_url='loginpage')
@admin_only
def jobpage(request):
	jobs = Jobs.objects.all()

	total_jobs = jobs.count()
	partnercompany = jobs.filter(status='Partner Company').count()
	jobseekers = jobs.filter(status='Job Seekers').count()

	context = {'jobs':jobs, 'total_jobs':total_jobs, 'partnercompany':partnercompany, 'jobseekers': jobseekers}

	return render(request, 'CITAT/adminjob.html', context)



@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def alumnipage(request, pk):
	alumni = Alumni.objects.get(id=pk)

	employed = alumni.employed_set.all() 
	
	context = {'alumni': alumni, 'employed': employed}
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

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['alumni'])
def employed(request):
	alumni = request.user.alumni
	form = EmployedModal()

	if request.method == "POST":
		form = EmployedModal(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.alumni = request.user.alumni
			instance.save()
			return redirect('account')

			


	context={'form': form}
	return render(request, 'CITAT/EmployedUser.html', context)


def updateprofile(request):

	context={}

	return render (request,'CITAT/updateprofile.html')





@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['alumni'])
def useremployed(request):
	alumni = request.user.alumni
	form = UserEmployed()

	if request.method == "POST":
		# form = UserEmployed(request.POST)
		# if form.is_valid():
		# 	form.save

		employed = request.POST["employed"]
		organization = request.POST["organization"]
		selections = request.POST["selections"]
		income = request.POST["income"]
		skills = request.POST["skills"]

		user_employed = UserEmployed(employed=employed,organization=organization,selections=selections,income=income,skills=skills)
		user_employed.save()
			


	context={'form' : form}
	return render(request, 'CITAT/User_Employed.html', context)




def navbar(request):
	alumni = Alumni.objects.all()


	context={'alumni': alumni}
	return render(request, 'CITAT/navbar.html', context)


def chatbot(request):

	context={}
	return render(request, 'CITAT/chatbot.html', context)

# def add_useremployed_form_submission(request):

# 	print("Hello, Employed form is submitted.")
# 	employed = request.POST["employed"]
# 	organization = request.POST["organization"]
# 	selections = request.POST["selections"]
# 	income = request.POST["income"]
# 	skills = request.POST["skills"]

# 	user_employed = UserEmployed(employed=employed,organization=organization,selections=selections,income=income,skills=skills)
# 	user_employed.save()

# 	return render(request, 'CITAT/User_Employed.html')
