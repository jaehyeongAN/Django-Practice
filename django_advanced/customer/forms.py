from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import Customer

class RegisterForm(forms.Form):
	email = forms.EmailField(
		error_messages = {
			'required' : '이메일을 입력해주세요.'
		},
		max_length=64, label='이메일')
	password = forms.CharField(
		error_messages = {
			'required' : '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label='비밀번호')
	re_password = forms.CharField(
		error_messages = {
			'required' : '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label='비밀번호 확인')

	def clean(self):
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		re_password = cleaned_data.get('re_password')

		if password and re_password:
			if password != re_password:
				self.add_error('password', '비밀번호가 서로 다릅니다.')
				self.add_error('re_password', '비밀번호가 서로 다릅니다.')
			else:
				customer = Customer(
					email = email,
					password = make_password(password)
					)
				customer.save()


class LoginForm(forms.Form):
	email = forms.EmailField(
		error_messages = {
			'required' : '이메일을 입력해주세요.'
		},
		max_length=64, label='이메일')
	password = forms.CharField(
		error_messages = {
			'required' : '비밀번호를 입력해주세요.'
		},
		widget=forms.PasswordInput, label='비밀번호')

	def clean(self):
		# 유효성 검사 
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')

		if email and password:
			try:
				customer = Customer.objects.get(email=email)
			except Customer.DoesNotExist:
				self.add_error('email','존재하지 않는 아이디 입니다.')
				return

			if not check_password(password, customer.password):
				# Customer 모델의 유저 비번과 html로부터 받은 비번이 다르면
				self.add_error('password', '비밀번호가 다릅니다!') # password 필드에 error 메시지 추가
			else:
				# 비번이 같으면 id를 넘김
				self.email = customer.email