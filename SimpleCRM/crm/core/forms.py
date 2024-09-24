# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	role = forms.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')], required=True)
	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password1', 'password2', 'role']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if CustomUser.objects.filter(email=email).exists():
			raise forms.ValidationError("A user with this email already exists.")
		return email

	def save(self, commit=True):
		user = super().save(commit=False)
		user.role = self.cleaned_data['role']
		if commit:
			user.save()
		return user
