from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.board_list),
	path('write/', views.board_write),
	path('detail/<int:pk>/', views.board_detail) # 숫자형으로 값을 받아 pk에 받은 후 board_detail()로 넘겨줌
]
