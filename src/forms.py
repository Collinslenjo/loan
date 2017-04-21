from django import forms

from .models import Loan

class PostForm(forms.ModelForm):
	class Meta:
		model = Loan
		fields = [
			"title",
			"content"
		]