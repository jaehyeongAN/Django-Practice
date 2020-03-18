from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
	boards = Board.objects.all().order_by('-id') # 모든 게시글을 최신순으로 가져옴
	return render(request, 'board_list.html', {'boards':boards})