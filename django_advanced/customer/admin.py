from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('email', ) # 뒤에 콤마를 꼭 써줘야함(안그러면 tuple로 인식을 못함)

admin.site.register(Customer, CustomerAdmin)