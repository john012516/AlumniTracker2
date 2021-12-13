from django.db import models

# Create your models here.
class Contact(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email=models.EmailField()
	subject=models.TextField()
	def __str__(self):
		return self.firstname

class Event(models.Model):
	EVENT = (
			('On-Going Events', 'On-Going Events'),
			('Upcoming Events', 'Upcoming Events'),
			('Completed Events', 'Completed Events'),
			 )
	Eventname = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(auto_now_add=True, null=True)
	time = models.CharField(max_length=200, null=True)
	when = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=EVENT)


class Jobs(models.Model):
	STATUS = (
			('Job Post', 'Job Post'),
			('Partner Company', 'Partner Company'),
			('job seekers', 'job seekers'),
			 )

	jobname = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


