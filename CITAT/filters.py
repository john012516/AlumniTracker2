import django_filters
from django_filters import DateFilter

from .models import *

class EventFilter(django_filters.FilterSet):
	# start_Date = DateFilter(field_name="date", lookup_expr='gte')
	# end_Date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Event
		fields = '__all__'
		exclude= ['date', 'time', 'place']

class GenderFilter(django_filters.FilterSet):
	class Meta:
		model = Alumni
		fields = ['firstname','lastname', 'Gender']

class CourseFilter(django_filters.FilterSet):
	class Meta:
		model = Alumni
		fields = ['firstname', 'lastname','Course']

class EmployedFilter(django_filters.FilterSet):
	class Meta:
		model = Alumni
		fields = ['firstname','lastname', 'alumni_employed']

class CountryFilter(django_filters.FilterSet):
	class Meta:
		model = Alumni
		fields = ['firstname','lastname', 'Country']

