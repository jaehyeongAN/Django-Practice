from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, DeleteView
from .models import Product
from .forms import RegisterForm

# Create your views here.

class ProductList(ListView):
	model = Product
	template_name = 'product.html'
	context_object_name = 'product_list' # object_list로도 사용가능하고 이름을 지정할 수 도 있음


class ProductCreate(FormView):
	template_name = 'register_product.html'
	form_class = RegisterForm
	success_url = '/product'

class ProductDetail(DeleteView):
	template_name = 'product_detail.html'
	queryset = Product.objects.all()
	context_object_name = 'product'