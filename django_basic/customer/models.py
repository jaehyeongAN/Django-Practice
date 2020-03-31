from django.db import models

# Create your models here.

class Customer(models.Model):
	customername = models.CharField(max_length=64, verbose_name='고객명')
	customeremail = models.CharField(max_length=128, verbose_name='고객이메일')
	password = models.CharField(max_length=32, verbose_name='비밀번호')
	registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

	def __str__(self):
		return self.customername

	class Meta:
		# 테이블 명 지정 
		db_table = 'django_customer'
		verbose_name = '고객정보'
		verbose_name_plural = '고객정보'

