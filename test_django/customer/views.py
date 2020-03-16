from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import Customer
from .forms import LoginForm

# Create your views here.

def home(request):
	user_id = request.session.get('user')
	if user_id:
		# login하여 session에 정보가 있을 경우
		customer = Customer.objects.get(pk=user_id) # primary key
		return HttpResponse(customer.customername)

	return HttpResponse('home!')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid(): # 유효성 검사 
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
	if request.method == 'GET':
		return render(request, 'register.html')

	elif request.method == 'POST':
		customername = request.POST.get('customername', None) # key값을 가져오는데 값이 없으면 None으로 지정 
		customeremail = request.POST.get('customeremail', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re-password', None)

		res_data = {}
		if not (customername and customeremail and password and re_password):
			# 값이 하나라도 입력이 안됐으면
			res_data['error'] = '모든 값을 입력해주세요!'
		elif password != re_password:
			# 비밀번호가 서로 다르면 
			res_data['error'] = '비밀번호가 일치하지 않습니다!'
		else:
			# 문제가 없을 경우 Admin에 추가 후 login.html로 이동 
			customer = Customer(
				customername = customername,
				customeremail = customeremail,
				password = make_password(password) # password를 암호화하여 저장
				)
			customer.save()
			return render(request, 'login.html')

		return render(request, 'register.html', res_data) # views에서 선언한 변수를 html로 전달
