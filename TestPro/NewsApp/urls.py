from django.urls import path
from .views import News,home,contact

urlpatterns = [
    path('news',News, name="News"),
    path('home', home,name="home"),
    path('contact',contact, name="contact"),
]
