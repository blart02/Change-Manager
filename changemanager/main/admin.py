from django.contrib import admin
from .models import ChangeRequest, ChangeRequestUpdate, Requestor, Service

# Register your models here.

admin.site.register(Service)
admin.site.register(Requestor)
admin.site.register(ChangeRequest)
admin.site.register(ChangeRequestUpdate)
