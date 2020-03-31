from django import forms

class BoardForm(forms.Form):
	title = forms.CharField(
		error_messages={
			'required': '제목을 입력해주세요.'
		},
		max_length=128, label='제목')
	contents = forms.CharField(
		error_messages={
			'required': '내용을 입력해주세요.'
		},
		widget=forms.Textarea, label='내용')
	tags = forms.CharField(
		required=False, # 태그를 입력하지 않아도 상관없도록
		label='태그')