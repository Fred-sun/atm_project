# /usr/bin/python env
# _*_ coding: utf-8 _*_
from django.shortcuts import HttpResponse


def index(request):
    print("This is test")
    return HttpResponse("This is index views")

def home(request):
    print("This is home page")
    return HttpResponse("Please enter your choice")