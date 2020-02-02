from django.shortcuts import render
from  .models import News
from .forms import RegistrationForm


# Create your views here.


def home(request):
    context={
    'name':'Parwiz Forogh'
    }
    return render(request,'home.html',context)

def Newp(request):
    obj=News.objects.get(id=1)
    context={
    'data':obj
    
     }
    return render(request,'news.html',context)


def NewsDate(request,year):
    article_list=News.objects.filter(pub_date_year=year)
    context={
    'year':year,
    'article_list':article_list,
    }
    return render(request,'newsdate.html',context)

def contact(request):
   
    return render(request,'contact.html')

def register(request):
    context={
        'form':RegistrationForm
    }
    return render(request,'signup.html')


