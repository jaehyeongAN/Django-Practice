from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Customer
from .forms import LoginForm, RegisterForm

# Create your views here.

def home(request):
	user_id = request.session.get('user')
	if user_id:
		# login하여 session에 정보가 있을 경우
		customer = Customer.objects.get(pk=user_id) # primary key(모델에 객체 생성 시 마다 순차적으로 고유한 값이 정해 짐(ex, 1,2,3,4,..))
		return HttpResponse(customer.customername)

	return HttpResponse('home!')

def login(request):
	if request.method == 'POST':
		# form 인스턴스를 생성하고 요청에 의한 데이터를 채움 (binding)
		form = LoginForm(request.POST)
		# form 유효성 체크 
		if form.is_valid(): 
			# form 입력이 정상적이면 session에 저장하고, 정상적이지 않을 경우엔 form에 error 메시지를 같이 넣어 전달 
			request.session['user'] = form.user_id # form에서 id를 가져옴
			return redirect('/') # root로 이동
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form':form}) # login.html로 form 전달 


def logout(request):
	if request.session.get('user'):
		# 값이 있으면
		del(request.session['user']) # 해당 세션 del

	return redirect('/')

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			# 유효성 검사 문제 없을 경우 Cutomer 모델에 추가
			customer = Customer(
				customername = form.data.get('customername'),
				customeremail = form.data.get('customeremail'),
				password = make_password(form.data.get('password')) # password를 암호화하여 저장
				)
			customer.save()
			return redirect('/')
	else:
		form = RegisterForm()

	return render(request, 'register.html', {'form':form})