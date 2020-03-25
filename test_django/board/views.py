from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from .forms import BoardForm
from customer.models import Customer

# Create your views here.

def board_list(request):
	boards = Board.objects.all().order_by('-id') # 모든 게시글을 최신순으로 가져옴
	return render(request, 'board_list.html', {'boards':boards})


def board_write(request):
	# 먼저 사용자를 확인하여 로그인을 안했을 경우 login페이지로 
	if not request.session.get('user'):
		return redirect('/customer/login')

	if request.method == 'POST':
		form = BoardForm(request.POST)
		if form.is_valid():
			# session에 저장된 user정보를 writer에 입력해줌  
			user_id = request.session.get('user')
			customer = Customer.objects.get(pk=user_id) 
 			
 			# Board 모델 (db) 저장 
			board = Board()
			board.title = form.cleaned_data['title']
			board.contents = form.cleaned_data['contents']
			board.writer = customer
			board.save()

			return redirect('/board/list')
	else:
		form = BoardForm()
	
	return render(request, 'board_write.html', {'form':form})

def board_detail(request, pk):
	try:
		board = Board.objects.get(pk=pk) # urls로 부터 넘어온 pk값을 통해 해당 객체를 get
	except Board.DoesNotExist: # 없는 페이지일 경우 
		raise Http404('게시글을 찾을 수 없습니다.')

	return render(request, 'board_detail.html', {'board':board})