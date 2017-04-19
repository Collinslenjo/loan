from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import Loan,Payments

# Create your views here.
#loan urlMaps
def index_loan(request):
	queryset = Loan.objects.all()
	context = {
			"title":"Homepage",
			"Loan_list":queryset
	}
	return render(request, "index.html", context)
	
#Loans for loan urlMap
def apply_loan(request):
	context = {
		"title":"Apply"
	}
	return render(request, "apply.html", context)
#Loan Details
def loan_details(request, id=None):
	instance = get_object_or_404(Loan, id=id)
	context = {
		"title": instance.title,
		"instance":instance
	}
	return render(request, "detail.html", context)
#Loan Types
def loan_types(request):
	context = {
		"title":"Types of loans"
	}
	return render(request, "loantypes.html", context)
#Payments
def payments(request):
	money = Payments.objects.all();
	context = {
		"title":"Payments",
		"pay_list": money
	}
	return render(request, "payments.html",context)
#Employees
def employees(request):
	context = {
		"title":"Employees"
	}
	return render(request, "employees.html",context)
#Company Setup
def company_setup(request):
	context = {
		"title":"Company setup"
	}
	return render(request, "company.html",context)
#Borrowers
def borrowers(request):
	context = {
	 	"title":"Borrowers"
	}
	return render(request, "borrowers.html",context)