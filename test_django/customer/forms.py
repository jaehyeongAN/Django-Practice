from django import forms
from .models import Customer
from django.contrib.auth.hashers import check_password, make_password

# from에서 해당 기능을 구현하고 클래스만 views.py에서 호출


class RegisterForm(forms.Form):
	customername = forms.CharField(
		error_messages={
			'required': '아이디를 입력해주세요.'
		},
		max_length=32, label='아이디를 입력해주세요.')
	customeremail = forms.CharField(
		error_messages={
			'required': '이메일을 입력해주세요.'
		},
		max_length=64, label='이메일을 입력해주세요.')
	password = forms.CharField(
		error_messages={
			'required': '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label='비밀번호를 입력해주세요.')
	re_password = forms.CharField(
		error_messages={
			'required': '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label='비밀번호를 입력해주세요.')

	def clean(self):
		cleaned_data = super().clean()
		customername = cleaned_data.get('customername')
		customeremail = cleaned_data.get('customeremail')
		password = cleaned_data.get('password')
		re_password = cleaned_data.get('re_password')

		if customername and customeremail and password and re_password:
			if password != re_password:
				self.add_error('password', '비밀번호가 서로 다릅니다!')
				self.add_error('re_password', '비밀번호가 서로 다릅니다!')


class LoginForm(forms.Form):
	customername = forms.CharField(
		error_messages={
			'required': '아이디를 입력해주세요.'
		}, 
		max_length=32, label="고객 이름")
	password = forms.CharField(
		error_messages={
			'required': '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label="비밀번호")

	def clean(self):
		# 유효성 검사 
		cleaned_data = super().clean()
		customername = cleaned_data.get('customername')
		password = cleaned_data.get('password')

		if customername and password:
			# html로부터 받은 customername과 같은 값을 Customer 모델에서 가져옴
			customer = Customer.objects.get(customername=customername)
			if not check_password(password, customer.password):
				# Customer 모델의 유저 비번과 html로부터 받은 비번이 다르면
				self.add_error('password', '비밀번호가 다릅니다!') # password 필드에 error 메시지 추가
			else:
				# 비번이 같으면 id를 넘김
				self.user_id = customer.id