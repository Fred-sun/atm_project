from django.shortcuts import render, HttpResponse

# Create your views here.

def atm_m_test(request):
    print("This is atm_m page")
    return HttpResponse("This is atm_m page")

def query_info(request):
    print("查询用户信息")
    return HttpResponse('Query user info')

def add_info(request):
    print("增加用户信息")
    return HttpResponse("Add user info")

def del_info(request):
    print("注销用户信息")
    return HttpResponse("Del user info")

def transfer_account(request):
    print("转账")
    return HttpResponse("Transfer account")

def withdrawal(request):
    print("提现")
    return HttpResponse("Withdrawal")

def reimbursement(request):
    print("还款")
    return HttpResponse("reimbursement")

def account_status(request):
    print("账户状况--冻结还是解冻")
    return HttpResponse("Freeze or thaw")

def print_bill(request):
    print("打印账单")
    return HttpResponse("Print the bill")

def shopping(request):
    print("结算")
    return HttpResponse("Shopping ")

