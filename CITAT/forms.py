from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *

class AlumniForm(ModelForm):
	class Meta:
		model = Alumni
		fields = '__all__'
		exclude = ['user']

class JobsForm(ModelForm):
	class Meta:
		model = Jobs
		fields = '__all__'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

class UserEmployedForm(ModelForm):
		models = UserEmployed
		fields = '__all__'

class UserUnEmployedForm(ModelForm):
		models = UserUnemployed
		fields = '__all__'

class UserSelfEmployedForm(ModelForm):
		models = UserSelfemployed
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required = False)
	last_name = forms.CharField(max_length=30, required = False)



	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
