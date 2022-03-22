from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *

class AlumniForm(ModelForm):
	# EMPLOYED = (
	# 	        ('Yes','Yes'),('No','No'),
	# 		   )
	# employed = forms.ChoiceField(choices=EMPLOYED, widget=forms.RadioSelect)

	class Meta:
		model = Alumni
		fields = '__all__'
		exclude = ['user']
		widgets={
		 	'incaseofemergency': forms.TextInput(attrs={'class':'form-control','placeholder':'Incase of Emergency'}),
		# 	'firstname' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'lastname' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'Gender' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'email' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'phone' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'address' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'zipcode' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'Course' : forms.TextInput(attrs={'class':'form-control'}),
		 }

class JobsForm(ModelForm):
	class Meta:
		model = Jobs
		fields = '__all__'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

#class UserEmployedForm(ModelForm):
		#models = UserEmployed
		#fields = '__all__'
class EmployedModal(ModelForm):
	class Meta:
		model = Employed
		fields = '__all__'
		exclude = ['alumni']

class UserEmployed(forms.ModelForm):
	EMPLOYED = (
		        ('Yes','Yes'), 
				('No','No'),
			   )
	employed = forms.ChoiceField(choices=EMPLOYED, widget=forms.RadioSelect)

	SKILLS = (
		      ('Yes','Yes'),
			  ('No', 'No'),
			 )
	skills = forms.ChoiceField(choices=SKILLS, widget=forms.RadioSelect)		 
	class Meta:
	    models = UserEmployed
	    fields = '__all__'		

class UserUnEmployedForm(forms.ModelForm):
	SEEK = (
		    ('Yes','Yes'),
			('No','No'),
	       )
	seek = forms.ChoiceField(choices=SEEK, widget=forms.RadioSelect)

	DESIRE = (
		      ('Yes','Yes'),
			  ('No', 'No'),
	         )	 
	desire = forms.ChoiceField(choices=DESIRE, widget=forms.RadioSelect)

	CONSIDER = (
		        ('Yes','Yes'),
				('No','No'),
	           )
	consider = forms.ChoiceField(choices=CONSIDER, widget=forms.RadioSelect)		   		   
	
	class Meta:
		models = UserUnemployed
		fields = '__all__'

class UserSelfEmployedForm(forms.ModelForm):
	RELATED = (
		       ('Yes','Yes'),
			   ('No','No'),
	          )
	related = forms.ChoiceField(choices=RELATED, widget=forms.RadioSelect)		  

	class Meta:
		models = UserSelfemployed
		fields = '__all__'
		

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required = False)
	last_name = forms.CharField(max_length=30, required = False)



	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

		#model = UserEmployed
		#fields = '__all__'
