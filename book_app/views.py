from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("index")
def login(request):
    return HttpResponse("login")
def safe_a(request):
    print('输出A安全等级的算法')
    return HttpResponse("实现了A等级的安全级别")
def sefa_b(request):
    print('输出B安全等级的算法')

    return HttpResponse("实现了B等级的安全级别")