from django.contrib import admin

from .models import Country, Indicator, MetaData

# Register your models here.

admin.site.register(Country)
admin.site.register(Indicator)
admin.site.register(MetaData)
