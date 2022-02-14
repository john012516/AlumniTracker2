from django.db import models

# Create your models here.
class Contact(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email=models.EmailField()
	subject=models.TextField()
	def __str__(self):
		return self.firstname

class Alumni(models.Model):
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	Gender = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email=models.EmailField()
	def __str__(self):
		return self.firstname

class Event(models.Model):
	EVENT = (
			('On-Going Events', 'On-Going Events'),
			('Upcoming Events', 'Upcoming Events'),
			('Completed Events', 'Completed Events'),
			 )
	Eventname = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(max_length=200, null=True)
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




