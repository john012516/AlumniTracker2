from django.contrib import admin
from .models import Carausel

# Register your models here.

from .models import *

admin.site.register(Alumni)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(JoinEvent)
admin.site.register(Jobs)
admin.site.register(Employed)


admin.site.register(Category)
admin.site.register(CompanyPhoto)

admin.site.register(Carausel)




