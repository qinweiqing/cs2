from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("index")
def login(request):
    return HttpResponse("login")
def safe_a(request):
    return HttpResponse("实现了A等级的安全级别")