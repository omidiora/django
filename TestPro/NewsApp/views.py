from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1>This is our HomePage</>')

def News(request):
    return HttpResponse('<h1>This is our lastest News</>')

def contact(request):
    return HttpResponse('<h1>This is our contact</>')


