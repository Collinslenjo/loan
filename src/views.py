from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#loan urlMaps
def index_loan(request):
	context = {
			"title":"Homepage"
	}
	return render(request, "index.html", context)
	
#Loans for loan urlMap
def apply_loan(request):
	context = {
		"title":"Apply"
	}
	return render(request, "apply.html", context)
#Loan Types
def loan_types(request):
	context = {
		"title":"Types of loans"
	}
	return render(request, "loantypes.html", context)
#Payments
def payments(request):
	context = {
		"title":"Payments"
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