from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.

def index(request):
	return render(request, 'index.html', {'email': request.session.get('user')})

class RegisterView(FormView):
	template_name = 'register.html' # 이동할 html
	form_class = RegisterForm # Form을 상속
	success_url = '/' # 성공 시 url

class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url = '/'

	# session 저장(유효성 검사가 성공일 때 수행)
	def form_valid(self, form):
		self.request.session['user'] = form.email
		return super().form_valid(form)
