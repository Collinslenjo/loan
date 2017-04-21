from django import forms

from .models import Loan

class PostFrom(forms.ModelForm):
	class Meta:
		model = Loan
		fields = [
			"title",
			"content"
		]