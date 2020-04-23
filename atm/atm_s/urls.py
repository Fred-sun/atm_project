# /usr/bin/python env
# _*_ coding: utf-8 _*_

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^atm_s/', views.atm_s_test),
    url(r'^add_cart/', views.add_cart),
    url(r'^view_cart/', views.view_cart),
    url(r'^settlement/', views.settlement),
    url(r'^record/', views.record),

]