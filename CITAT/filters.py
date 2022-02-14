import django_filters
from django_filters import DateFilter

from .models import Event

class EventFilter(django_filters.FilterSet):
	# start_Date = DateFilter(field_name="date", lookup_expr='gte')
	# end_Date = DateFilter(field_name="date", lookup_expr='lte')
	class Meta:
		model = Event
		fields = '__all__'
		exclude= ['date', 'time', 'place']

