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
	return render(request, "apply.html", {})
#Loan Types
def loan_types(request):
	return render(request, "loantypes.html", {})
#Payments
def payments(request):
	return render(request, "payments.html",{})
#Employees
def employees(request):
	return render(request, "employees.html",{})
#Company Setup
def company_setup(request):
	return render(request, "company.html",{})
#Borrowers
def borrowers(request):
	return render(request, "borrowers.html",{})