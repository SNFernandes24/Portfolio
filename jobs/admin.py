from django.contrib import admin
from .models import Job
from .models import Description
# Register your models here.

admin.site.register(Job)
admin.site.register(Description)
