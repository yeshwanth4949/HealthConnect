from django import forms
from .models import UserLogin

class UserLoginForm(forms.ModelForm):
	class Meta:
		model=UserLogin
		fields="__all__"
		labels={
		'username':"Enter Username",
		'password':"Enter Password",
		}


