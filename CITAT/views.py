from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only




from .models import Carausel




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
def genderstatus(request):
	alumni = Alumni.objects.all()

	myFilter = GenderFilter(request.GET, queryset=alumni)
	alumni = myFilter.qs

	total_alumni = alumni.count()
	male = alumni.filter(Gender='MALE').count()
	female = alumni.filter(Gender='FEMALE').count()

	context = {'alumni': alumni, 'total_alumni': total_alumni, 'male': male, 'female': female, 'myFilter': myFilter}
	return render(request, 'CITAT/Gender.html', context)

@login_required(login_url='loginpage')
@admin_only
def coursestatus(request):
	alumni = Alumni.objects.all()

	myFilter = CourseFilter(request.GET, queryset=alumni)
	alumni = myFilter.qs


	bsit = alumni.filter(Course="BSIT").count()
	bscs = alumni.filter(Course="BSCS").count()

	context = {'alumni': alumni, 'bsit': bsit, 'bscs': bscs,'myFilter': myFilter}
	return render(request, 'CITAT/Course.html', context)


@login_required(login_url='loginpage')
@admin_only
def employedstatus(request):
	alumni = Alumni.objects.all()

	myFilter = EmployedFilter(request.GET, queryset=alumni)
	alumni = myFilter.qs

	emp = alumni.filter(alumni_employed="Employed").count()
	unemp = alumni.filter(alumni_employed="Unemployed").count()
	selfemp = alumni.filter(alumni_employed="Self-employed").count()

	context = {'alumni': alumni, 'emp': emp, 'unemp': unemp, 'selfemp': selfemp, 'myFilter': myFilter}
	return render(request, 'CITAT/EmployedStatus.html', context)

@login_required(login_url='loginpage')
@admin_only
def countrystatus(request):
	alumni = Alumni.objects.all()
	employed = Employed.objects.all()

	myFilter = CountryFilter(request.GET, queryset=alumni)
	alumni = myFilter.qs

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

	Honduras = alumni.filter(Country="Honduras").count()
	Haiti = alumni.filter(Country="Haiti").count()
	HongKong = alumni.filter(Country="Hong Kong").count()
	Hungary = alumni.filter(Country="Hungary").count()
	Iceland = alumni.filter(Country="Iceland").count()
	Indonesia = alumni.filter(Country="Indonesia").count()
	India = alumni.filter(Country="India").count()
	Iran = alumni.filter(Country="Iran").count()
	Iraq = alumni.filter(Country="Iraq").count()
	Ireland = alumni.filter(Country="Ireland").count()
	IsleofMan = alumni.filter(Country="Isle of Man").count()
	Israel = alumni.filter(Country="Israel").count()
	Italy = alumni.filter(Country="Italy").count()
	Jamaica = alumni.filter(Country="Jamaica").count()
	Japan = alumni.filter(Country="Japan").count()
	Jordan = alumni.filter(Country="Jordan").count()
	Kazakhstan = alumni.filter(Country="Kazakhstan").count()
	Kenya = alumni.filter(Country="Kenya").count()
	Kiribati = alumni.filter(Country="Kiribati").count()
	KoreaNorth = alumni.filter(Country="Korea North").count()
	KoreaSouth = alumni.filter(Country="Korea South").count()
	Kuwait = alumni.filter(Country="Kuwait").count()
	Kyrgyzstan = alumni.filter(Country="Kyrgyzstan").count()
	Laos = alumni.filter(Country="Laos").count()
	Latvia = alumni.filter(Country="Latvia").count()
	Lebanon = alumni.filter(Country="Lebanon").count()
	Lesotho = alumni.filter(Country="Lesotho").count()
	Liberia = alumni.filter(Country="Liberia").count()
	Liechtenstein = alumni.filter(Country="Liechtenstein").count()
	Lithuania = alumni.filter(Country="Lithuania").count()
	Luxembourg = alumni.filter(Country="Luxembourg").count()
	Macau = alumni.filter(Country="Macau").count()
	Macedonia = alumni.filter(Country="Macedonia").count()
	Madagascar = alumni.filter(Country="Madagascar").count()
	Malaysia = alumni.filter(Country="Malaysia").count()
	Malawi = alumni.filter(Country="Malawi").count()
	Maldives = alumni.filter(Country="Maldives").count()
	Mali = alumni.filter(Country="Mali").count()
	Malta = alumni.filter(Country="Malta").count()
	MarshallIslands = alumni.filter(Country="Marshall Islands").count()
	Martinique = alumni.filter(Country="Martinique").count()
	Mauritania = alumni.filter(Country="Mauritania").count()
	Mauritius = alumni.filter(Country="Mauritius").count()
	Mayotte = alumni.filter(Country="Mayotte").count()
	Mexico = alumni.filter(Country="Mexico").count()
	Midway = alumni.filter(Country="Midway").count()
	Moldova = alumni.filter(Country="Moldova").count()
	Monaco = alumni.filter(Country="Monaco").count()
	Mongolia = alumni.filter(Country="Mongolia").count()
	Montserrat = alumni.filter(Country="Montserrat").count()
	Morocco = alumni.filter(Country="Morocco").count()
	Mozambique = alumni.filter(Country="Mozambique").count()
	Myanmar = alumni.filter(Country="Myanmar").count()
	Nambia = alumni.filter(Country="Nambia").count()
	Nauru = alumni.filter(Country="Nauru").count()
	Nepal = alumni.filter(Country="Nepal").count()
	NetherlandAntilles = alumni.filter(Country="Netherlands (Holland, Europe) Antilles").count()
	NetherlandsHollandEurope = alumni.filter(Country="Guyana").count()
	Nevis = alumni.filter(Country="Nevis").count()
	NewCaledonia = alumni.filter(Country="New Caledonia").count()
	NewZealand = alumni.filter(Country="New Zealand").count()
	Nicaragua = alumni.filter(Country="Nicaragua").count()
	Niger = alumni.filter(Country="Niger").count()
	Nigeria = alumni.filter(Country="Nigeria").count()
	Niue = alumni.filter(Country="Niue").count()
	NorfolkIsland = alumni.filter(Country="Norfolk Island").count()
	Norway = alumni.filter(Country="Norway").count()
	Oman = alumni.filter(Country="Oman").count()
	Pakistan = alumni.filter(Country="Pakistan").count()
	PalauIsland = alumni.filter(Country="Palau Island").count()
	Palestine = alumni.filter(Country="Palestine").count()
	Panama = alumni.filter(Country="Panama").count()
	PapuaNewGuinea = alumni.filter(Country="Papua New Guinea").count()
	Paraguay = alumni.filter(Country="Paraguay").count()
	Peru = alumni.filter(Country="Peru").count()
	Philippines = alumni.filter(Country="Philippines").count()
	PitcairnIsland = alumni.filter(Country="Pitcairn Island").count()
	Poland = alumni.filter(Country="Poland").count()
	Portugal = alumni.filter(Country="Portugal").count()
	PuertoRico = alumni.filter(Country="Puerto Rico").count()
	Qatar = alumni.filter(Country="Qatar").count()
	RepublicofMontenegro = alumni.filter(Country="Republic of Montenegro").count()
	RepublicofSerbia = alumni.filter(Country="Republic of Serbia").count()
	Romania = alumni.filter(Country="Romania").count()
	Russia = alumni.filter(Country="Russia").count()
	StBarthelemy = alumni.filter(Country="St Barthelemy").count()
	StEustatius = alumni.filter(Country="St Eustatius").count()
	StHelena = alumni.filter(Country="St Helena").count()
	StKittsNevis = alumni.filter(Country="St Kitts-Nevis").count()
	StLucia = alumni.filter(Country="St Lucia").count()
	StMaarten = alumni.filter(Country="St Maarten").count()
	StPierreandMiquelon = alumni.filter(Country="St Pierre & Miquelon").count()
	StVincentandGrenadines = alumni.filter(Country="St Vincent & Grenadines").count()
	Saipan = alumni.filter(Country="Saipan").count()
	Samoa = alumni.filter(Country="Samoa").count()
	SamoaAmerican = alumni.filter(Country="Samoa American").count()
	SanMarino = alumni.filter(Country="San Marino").count()
	SaoTomeandPrincipe = alumni.filter(Country="Sao Tome & Principe").count()
	SaudiArabia = alumni.filter(Country="Saudi Arabia").count()
	Senegal = alumni.filter(Country="Senegal").count()
	Seychelles = alumni.filter(Country="Seychelles").count()
	SierraLeone = alumni.filter(Country="Sierra Leone").count()
	Singapore = alumni.filter(Country="Singapore").count()
	Slovakia = alumni.filter(Country="Slovakia").count()
	Slovenia = alumni.filter(Country="Slovenia").count()
	SolomonIslands = alumni.filter(Country="SolomonIslands").count()
	Somalia = alumni.filter(Country="Somalia").count()
	SouthAfrica = alumni.filter(Country="South Africa").count()
	Spain = alumni.filter(Country="Spain").count()
	SriLanka = alumni.filter(Country="Sri Lanka").count()
	Sudan = alumni.filter(Country="Sudan").count()
	Suriname = alumni.filter(Country="Suriname").count()
	Swaziland = alumni.filter(Country="Swaziland").count()
	Sweden = alumni.filter(Country="Sweden").count()
	Switzerland = alumni.filter(Country="Switzerland").count()
	Syria = alumni.filter(Country="Syria").count()
	Tahiti = alumni.filter(Country="Tahiti").count()
	Taiwan = alumni.filter(Country="Taiwan").count()
	Tajikistan = alumni.filter(Country="Tajikistan").count()
	Tanzania = alumni.filter(Country="Tanzania").count()
	Thailand = alumni.filter(Country="Thailand").count()
	Togo = alumni.filter(Country="Togo").count()
	Tokelau = alumni.filter(Country="Tokelau").count()
	Tonga = alumni.filter(Country="Tonga").count()
	TrinidadandTobago = alumni.filter(Country="Trinidad & Tobago").count()
	Tunisia = alumni.filter(Country="Tunisia").count()
	Turkey = alumni.filter(Country="Turkey").count()
	Turkmenistan = alumni.filter(Country="Turkmenistan").count()
	TurksandCaicosIs = alumni.filter(Country="Turks & Caicos Is").count()
	Tuvalu = alumni.filter(Country="Tuvalu").count()
	Uganda = alumni.filter(Country="Uganda").count()
	UnitedKingdom = alumni.filter(Country="United Kingdom").count()
	Ukraine = alumni.filter(Country="Ukraine").count()
	UnitedArabEmirates = alumni.filter(Country="United Arab Emirates").count()
	UnitedStatesofAmerica = alumni.filter(Country="United States of America").count()
	Uruguay = alumni.filter(Country="Uruguay").count()
	Uzbekistan = alumni.filter(Country="Uzbekistan").count()
	Vanuatu = alumni.filter(Country="Vanuatu").count()
	VaticanCityState = alumni.filter(Country="Vatican City State").count()
	Venezuela = alumni.filter(Country="Venezuela").count()
	Vietnam = alumni.filter(Country="Vietnam").count()
	VirginIslandsBrit = alumni.filter(Country="Virgin Islands (Brit)").count()
	VirginIslandsUSA = alumni.filter(Country="Virgin Islands (USA)").count()
	WakeIsland = alumni.filter(Country="Wake Island").count()
	WallisandFutanaIs = alumni.filter(Country="Wallis & Futana Is").count()
	Yemen = alumni.filter(Country="Yemen").count()
	Zaire = alumni.filter(Country="Zaire").count()
	Zambia = alumni.filter(Country="Zambia").count()
	Zimbabwe = alumni.filter(Country="Zimbabwe").count()
	









	context = {'alumni':alumni, 'myFilter': myFilter, 'employed': employed,

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
	'Guadeloupe': Guadeloupe, 'Guam': Guam, 'Guatemala': Guatemala, 'Guinea': Guinea, 'Guyana': Guyana,

	'Honduras': Honduras,'Haiti': Haiti,'HongKong': HongKong,'Hungary': Hungary,

	'Iceland': Iceland,'Indonesia': Indonesia,'India': India,'Iran': Iran,'Iraq': Iraq,'Ireland': Ireland, 'IsleofMan': IsleofMan,'Israel': Israel,'Italy': Italy,

	'Jamaica': Jamaica,'Japan': Japan,'Jordan': Jordan,

	'Kazakhstan': Kazakhstan,'Kenya': Kenya,'Kiribati': Kiribati,'KoreaNorth': KoreaNorth, 'KoreaSouth': KoreaSouth,'Kuwait': Kuwait,'Kyrgyzstan': Kyrgyzstan,

	'Laos': Laos,'Latvia': Latvia,'Lebanon': Lebanon,'Lesotho': Lesotho,'Liberia': Liberia,'Liechtenstein': Liechtenstein,'Lithuania': Lithuania, 'Luxembourg': Luxembourg,

	'Macau': Macau,'Macedonia': Macedonia,'Madagascar': Madagascar,'Malaysia': Malaysia,'Malawi': Malawi,'Maldives': Maldives,'Mali': Mali,'Malta': Malta,'MarshallIslands': MarshallIslands,
	'Martinique': Martinique,'Mauritania': Mauritania,'Mauritius': Mauritius,'Mayotte': Mayotte,'Mexico': Mexico,'Midway': Midway,'Moldova': Moldova,'Monaco': Monaco,'Mongolia': Mongolia,'Montserrat': Montserrat,
	'Morocco': Morocco,'Mozambique': Mozambique,'Myanmar': Myanmar,

	'Nambia': Nambia,'Nauru': Nauru,'Nepal': Nepal,'NetherlandAntilles': NetherlandAntilles,'NetherlandsHollandEurope': NetherlandsHollandEurope,'Nevis': Nevis,'NewCaledonia': NewCaledonia,
	'NewZealand': NewZealand,'Nicaragua': Nicaragua,'Niger': Niger,'Nigeria': Nigeria,'Niue': Niue,'NorfolkIsland': NorfolkIsland,'Norway': Norway,

	'Oman': Oman,

	'Pakistan': Pakistan,'PalauIsland': PalauIsland, 'Palestine': Palestine,'Panama': Panama,'PapuaNewGuinea': PapuaNewGuinea,'Paraguay': Paraguay,'Peru': Peru,'Philippines': Philippines,
	'PitcairnIsland': PitcairnIsland,'Poland': Poland,'Portugal': Portugal,'PuertoRico': PuertoRico,

	'Qatar': Qatar,

	'RepublicofMontenegro': RepublicofMontenegro,'RepublicofSerbia': RepublicofSerbia,'Romania': Romania,'Russia': Russia,

	'StBarthelemy': StBarthelemy,'StEustatius': StEustatius,'StHelena': StHelena,'StKittsNevis': StKittsNevis,'StLucia': StLucia,
	'StMaarten': StMaarten, 'StPierreandMiquelon': StPierreandMiquelon,'StVincentandGrenadines': StVincentandGrenadines,'Saipan': Saipan,'Samoa': Samoa,'SamoaAmerican': SamoaAmerican,
	'SanMarino': SanMarino,'SaoTomeandPrincipe': SaoTomeandPrincipe,'SaudiArabia': SaudiArabia,'Senegal': Senegal,'Seychelles': Seychelles,
	'SierraLeone': SierraLeone,'Singapore': Singapore,'Slovakia': Slovakia,'Slovenia': Slovenia,'SolomonIslands': SolomonIslands,'Somalia': Somalia,'SouthAfrica': SouthAfrica,'Spain': Spain,
	'SriLanka': SriLanka,'Sudan': Sudan,'Suriname': Suriname, 'Swaziland': Swaziland,'Sweden': Sweden,'Switzerland': Switzerland,'Syria': Syria,

	'Tahiti': Tahiti,'Taiwan': Taiwan,'Tajikistan': Tajikistan,'Tanzania': Tanzania,'Thailand': Thailand, 'Togo': Togo,'Tokelau': Tokelau,'Tonga': Tonga,'TrinidadandTobago': TrinidadandTobago,
	'Tunisia': Tunisia,'Turkey': Turkey,'Turkmenistan': Turkmenistan,'TurksandCaicosIs': TurksandCaicosIs,'Tuvalu': Tuvalu,

	'Uganda': Uganda, 'UnitedKingdom': UnitedKingdom,'Ukraine': Ukraine,'UnitedArabEmirates': UnitedArabEmirates,'UnitedStatesofAmerica': UnitedStatesofAmerica,'Uruguay': Uruguay,'Uzbekistan': Uzbekistan,
	
	'Vanuatu': Vanuatu,'VaticanCityState': VaticanCityState,'Venezuela': Venezuela,'Vietnam': Vietnam,
	'VirginIslandsBrit': VirginIslandsBrit,'VirginIslandsUSA': VirginIslandsUSA,

	'WakeIsland': WakeIsland,'WallisandFutanaIs': WallisandFutanaIs,

	'Yemen': Yemen,

	'Zaire': Zaire,'Zambia': Zambia,'Zimbabwe': Zimbabwe

	}
	return render(request, 'CITAT/Country.html', context)



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
	
    
	context = {'jobs':jobs, 'alumni':alumni, 'total_alumni':total_alumni, 'male':male, 'female': female, 
	'bsit': bsit, 'bscs': bscs, 'emp': emp, 'unemp': unemp, 'selfemp': selfemp, 'employed': employed}

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
		messages.success(request, 'Successfully Submitted')
		return redirect('account')

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
			messages.success(request, 'Successfully Submitted')
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

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def companygallery(request):
	category = request.GET.get('category')
	if category == None:
		photos = CompanyPhoto.objects.all()
	else:
		photos = CompanyPhoto.objects.filter(category__name__contains=category)

	categories = Category.objects.all()	

	context={'categories': categories, 'photos': photos}
	return render(request, 'CITAT/CompanyGallery.html', context)



@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def viewcompany(request, pk):

	photos = CompanyPhoto.objects.get(id=pk)

	
	return render(request, 'CITAT/ViewCompany.html', {'photos': photos})


@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['alumni'])
def addcompany(request):
	categories = Category.objects.all()

	if request.method == 'POST':
		data=request.POST
		image=request.FILES.get('image')

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])
		elif data['category_new'] != '':
			category, created = Category.objects.get_or_create(name=data['category_new'])
		else: 
			category = None

		photo = CompanyPhoto.objects.create(
				category=category,
				firstname=data['firstname'],
				lastname=data['lastname'],
				Company_address=data['address'],
				Company_zipcode=data['zipcode'],
				Company_contact=data['contact'],
				Company_email=data['email'],
				Position=data['position'],
				Income=data['Income'],
				Year_started=data['yearstarted'],
				Company_pic=image,
			)
		messages.success(request, 'Successfully Submitted')
		return redirect('account')

	context={'categories': categories}
	return render(request, 'CITAT/AddingCompany.html', context)

def Home(request):

	obj = Carausel.objects.all()
	context = {
		'obj':obj
	}
	return render(request, 'CITAT/Home.html', context)	


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
