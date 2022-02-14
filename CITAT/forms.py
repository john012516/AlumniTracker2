from django.forms import ModelForm
from .models import *

class JobsForm(ModelForm):
	class Meta:
		model = Jobs
		fields = '__all__'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'