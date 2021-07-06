from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'shop1/index.html')

def about(request):
    return render(request,'shop1/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def productview(request):
    return HttpResponse("We are at product view")

def search(request):
    return HttpResponse("We are at search")

def checkout(request):
    return HttpResponse("We are at checkout")


