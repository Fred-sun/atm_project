# /usr/bin/python env
# _*_ coding: utf-8 _*_

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^atm_m/', views.atm_m_test),
    url(r'^query_info/',views.query_info),
    url(r'^add_info/', views.add_info),
    url(r'^del_info/', views.del_info),
    url(r'^transfer_account/', views.transfer_account),
    url(r'^withdrawal/', views.withdrawal),
    url(r'^reimbursement/', views.reimbursement),
    url(r'^account_status/', views.account_status),
    url(r'^print_bill/', views.print_bill),
    url(r'^shopping/', views.shopping),


]