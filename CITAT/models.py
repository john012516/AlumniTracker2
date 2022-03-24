from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
#from django.db.models import ChoiceField

# Create your models here.
class Contact(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email=models.EmailField()
	subject=models.TextField()
	def __str__(self):
		return self.firstname

class Alumni(models.Model):
	STATUS = (
			 ('Employed', 'Employed'),
			 ('Unemployed', 'Unemployed'),
			 ('Self-employed', 'Self-employed'),
			)
	CIVIL = (
			('Single','Single'),
			('Married', 'Married'),
			('Widowed', 'Widowed'),
			)
	INCOME = (
			('10,000-25,000','10,000-25,000'),
			('30,000-40,000', '30,000-40,000'),
			('50,000-70,000', '50,000-70,000'),
			('More than the choices', 'More than the choices'),
			)
	GENDER = (
			('MALE', 'MALE'),
			('FEMALE', 'FEMALE'),
			)
	user = models.OneToOneField(User, null =True,blank=True, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	Gender = models.CharField(max_length=200, null=True, choices=GENDER)
	Civil = models.CharField(max_length=200, null=True, choices=CIVIL)
	email=models.EmailField()
	Telephone = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	Religion = models.CharField(max_length=200, null=True)
	Citizenship = models.CharField(max_length=200, null=True)
	Date_of_Birth = models.CharField(max_length=200, null=True)
	Place_of_Birth = models.CharField(max_length=200, null=True)
	Course = models.CharField(max_length=200, null=True,)

	incaseofemergency = models.CharField(max_length=200, null=True, editable=False)
	nameofemergency = models.CharField(max_length=200, null=True,)
	relation = models.CharField(max_length=200, null=True,)
	contactnumber = models.CharField(max_length=200, null=True,)
	address2 = models.CharField(max_length=200, null=True,)

	alumni_employed=models.CharField(max_length=200, null=True, choices=STATUS)


	profile_pic = models.ImageField(default="default.png", null=True, blank=True ) 



	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.firstname


class Event(models.Model):
	EVENT = (
			('On-Going Events', 'On-Going Events'),
			('Upcoming Events', 'Upcoming Events'),
			('Completed Events', 'Completed Events'),
			 )
	Eventname = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(max_length=200, auto_now_add=True, null=True)
	time = models.CharField(max_length=200, null=True)
	place = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=EVENT)

	def __str__(self):
		return self.Eventname


class JoinEvent(models.Model):
	alumni = models.ForeignKey(Alumni, null=True, on_delete=models.SET_NULL)
	firstname = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	eventname = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.firstname



class Jobs(models.Model):
	STATUS = (
			('Job Post', 'Job Post'),
			('Partner Company', 'Partner Company'),
			('job seekers', 'job seekers'),
			 )

	jobname = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	
	def __str__(self):
		return self.jobname

class UserEmployed(models.Model):
	#user = models.OneToOneField(User, null =True,blank=True, on_delete=models.CASCADE)
	#employed_yes=models.BooleanField("Yes", default=False)
	#employed_no=models.BooleanField("No", default=False)
	 
	ORGANIZATION = (
					('--Select--', '--Select--'),
					('Government Organization (GO)', 'Government Organization (GO)'),
					('Business Organization (BO)', 'Business Organization (BO)'),
					('Private Organization', 'Private Organization'),
					('Cooperative', 'Cooperative'),
					('Non Government Organization', 'Non Government Organization'),
					('Peoples Organization', 'Peoples Organization'),
					)
	SELECTIONS = (
					('--Select--', '--Select--'),
					('Selection', 'Selection'),
					('Retention', 'Retention'),
					('Promotion', 'Promotion'),
			)

	alumni = models.ForeignKey(Alumni, null=True, on_delete=models.SET_NULL)
	employed=models.CharField(max_length=200, null=True) 			
	organization = models.CharField(max_length=200, null=True, choices=ORGANIZATION)
	selections = models.CharField(max_length=200, null=True, choices=SELECTIONS)
	income = models.CharField(max_length=200, null=True)
	#skill_yes=models.BooleanField("Yes", default=False)
	#skill_no=models.BooleanField("No", default=False)
	skills=models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.organization


class UserUnemployed(models.Model):
	#user = models.OneToOneField(User, null =True,blank=True, on_delete=models.CASCADE)
	REASON = (
			('--Select--', '--Select--'),
			('I cannot find a good job', 'I cannot find a good job'),
			('advance or further study first', 'advance or further study first'),
			('i do not like to be tied with a job and have a boss', 'i do not like to be tied with a job and have a boss'),
			('Advise of husband/wife or relatives', 'Advise of husband/wife or relatives'),
			('No job opportunity', 'No job opportunity'),
			('Health-related reasons', 'Health-related reasons'),
			('Family concern and decided no to find a job', 'Family concern and decided no to find a job'),
			('I want to put my own business', 'I want to put my own business'),
			('I want to be of my own', 'I want to be of my own'),
			('Lack of work experience', 'Lack of work experience'),
			('Did not look for job', 'Did not look for job'),
			('Others', 'Others'),
			)
	
	FINANCE = (
				('--Select--', '--Select--'),
				('Supported by parents', 'Supported by parents'),
				('Supported by relatives/brothers/sisters', 'Supported by relatives/brothers/sisters'),
				('Do buy and sell', 'Do buy and sell'),
				('Supported by husband/wife', 'Supported by husband/wife'),
				('Farm laborer of other farms', 'Farm laborer of other farms'),
				('Entered as domestic helper', 'Entered as domestic helper'),
				('Others', 'Others'),
				)

	reasons = models.CharField(max_length=200, null=True, choices=REASON)
	#job_yes = models.BooleanField("Yes", default=False)
	#job_no = models.BooleanField("NO", default=False) 
	seek=models.CharField(max_length=50, null=True)
	aftergrad = models.CharField(max_length=200, null=True)

	finance = models.CharField(max_length=200, null=True, choices=FINANCE)
	#desire_yes = models.BooleanField("Yes", default=False)
	#desire_no = models.BooleanField("No", default=False)
	desire = models.CharField(max_length=50, null=True)
	consider= models.CharField(max_length=50, null=True)




class UserSelfemployed(models.Model):
	#user = models.OneToOneField(User, null =True,blank=True, on_delete=models.CASCADE)
	BUSINESS = (
				('--Select--', '--Select--'),
				('Direct Selling', 'Direct Selling'),
				('Farming', 'Farming'),
				('Fishing', 'Fishing'),
				('Franchise', 'Franchise'),
				('Franchising', 'Franchising'),
				('Service Operation', 'Service Operation'),
				('Trading', 'Trading'),
				('Others', 'Others'),
				)

	business = models.CharField(max_length=200, null=True, choices=BUSINESS)
	#related_yes = models.BooleanField("Yes", default=False)
	#related_no = models.BooleanField("No", default=False)
	related = models.CharField(max_length=50, null=True)
	REASON = (
			('Higher Income', 'Higher Income'),
			('More Flexible Time', 'More Flexible Time'),
			('Family Affair', 'Family Affair'),
			('Had the opportunity to put up my business', 'Had the opportunity to put up my business'),
			('Advised by husband/wife/relatives', 'Advised by husband/wife/relatives'),
			('To have time to attend household chores', 'To have time to attend household chores'),
			('I want to be the boss of my own', 'I want to be the boss of my own'),
			('Others', 'Others'),
			)
	reason = models.CharField(max_length=200, null=True, choices=REASON)
	numberofemployee = models.CharField(max_length=200, null=True)
	skills = models.CharField(max_length=200, null=True)


class Employed(models.Model):

	INCOME = (
			('10,000-25,000','10,000-25,000'),
			('30,000-40,000', '30,000-40,000'),
			('50,000-70,000', '50,000-70,000'),
			('More than the choices', 'More than the choices'),
			)
			
	alumni = models.ForeignKey(Alumni, null=True, on_delete=models.SET_NULL)
	Company_name = models.CharField(max_length=200, null=True)
	Company_address = models.CharField(max_length=200, null=True)
	Company_zipcode = models.CharField(max_length=200, null=True)
	Company_contact = models.CharField(max_length=200, null=True)
	Company_email = models.CharField(max_length=200, null=True)
	Position = models.CharField(max_length=200, null=True)
	Income = models.CharField(max_length=200, null=True, choices=INCOME)
	Year_started = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.Company_name










