from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Alumni)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(JoinEvent)
admin.site.register(Jobs)
admin.site.register(UserEmployed)
admin.site.register(UserUnemployed)
admin.site.register(UserSelfemployed)
admin.site.register(Employed)
