from django.shortcuts import render, HttpResponse

# Create your views here.

def atm_s_test(request):
    print("This is atm_s page")
    return HttpResponse("This is atm_s page")

def add_cart(request):
    print("加入购物车")
    return HttpResponse("Add to cart")

def view_cart(request):
    print("查看购物车")
    return HttpResponse("Query cart info")

def settlement(request):
    print("结算")
    return HttpResponse("Settlement")

def record(request):
    print("记录日志")
    return HttpResponse("Record purchase log")