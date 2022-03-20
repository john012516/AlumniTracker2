from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Alumni


def alumni_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='alumni')
		instance.groups.add(group)

		Alumni.objects.create(
			user=instance,
			firstname=instance.first_name,
			lastname=instance.last_name,
			email=instance.email,
			)		
		print('Profile Created!')


post_save.connect(alumni_profile, sender=User)


