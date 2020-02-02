from django.contrib import admin

# Register your models here.
from .models import News,SportNews,RegistraionData

admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(RegistraionData)

