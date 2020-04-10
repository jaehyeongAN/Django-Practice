from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.

class OrderCreate(FormView):
	# ProductDetail에서 form을 받기 때문에 template_name이 필요하지 않음
	form_class = RegisterForm
	success_url = '/product/'