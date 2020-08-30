from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("index")
def login(request):
    return HttpResponse("login")
def sefa_b(request):
    return HttpResponse("实现了B等级的安全级别")