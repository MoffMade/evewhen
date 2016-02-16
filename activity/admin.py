from django.contrib import admin
from .models import Pilot, Corporation, Alliance
# Register your models here.

admin.site.register(Pilot)
admin.site.register(Corporation)
admin.site.register(Alliance)

