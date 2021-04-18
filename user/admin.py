from django.contrib import admin
from .models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ("tasks", )

admin.site.register(Person, PersonAdmin)
admin.site.register(Task)