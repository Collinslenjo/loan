"""Loan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from material.frontend import urls as frontend_urls

from src.views import (
	index_loan,
	apply_loan,
    loan_details,
    loan_types,
    payments,
    employees,
    company_setup,
    borrowers,
	)

urlpatterns = [
    url(r'^$', index_loan),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loan/apply/$', apply_loan, name='loan'),
    url(r'^loan/details/(?P<id>\d+)/$', loan_details, name='details'),
    url(r'^loan/types/$', loan_types, name='loantype'),
    url(r'^loan/payments/$', payments, name = 'payment'),
    url(r'^loan/employees/$',employees, name = 'employee'),
    url(r'^loan/company/$',company_setup, name = 'company'),
    url(r'^loan/borrowers/$', borrowers, name = 'borrower'),
    url(r'', include(frontend_urls)),
]

 # if settings.DEBUG:
 #     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)