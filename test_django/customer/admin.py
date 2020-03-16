from django.contrib import admin
from .models import Customer

# Register your models here.

class customerAdmin(admin.ModelAdmin):
	list_display = ['customername', 'password']

admin.site.register(Customer, customerAdmin)
