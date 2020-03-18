from django.db import models

# Create your models here.

class Board(models.Model):
	title = models.CharField(max_length=128, verbose_name='제목')
	contents = models.TextField(verbose_name='내용')
	# on_delete 매개변수 : models.CASCADE / models.SET_NULL / models.SET_DEFAULT
	writer = models.ForeignKey('customer.Customer', # 참조하는 모델 
									on_delete=models.CASCADE, # Customer모델의 사용자가 탈퇴하면 사용자의 모든 글 삭제
									verbose_name='작성자')
	registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'django_board'
		verbose_name = '사용자 게시글'
		verbose_name_plural = '사용자 게시글'