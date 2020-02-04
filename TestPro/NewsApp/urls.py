from django.urls import path
from .views import Newp,home,contact,NewsDate,register,addUser, modelform,addModalForm
urlpatterns = [
    path('news',Newp, name="news"),
    path('', home,name="home"),
    path('contact/',contact, name="contact"),
    path('newsdate/<int:year>',NewsDate, name="newsdate"),
    path('signup/',register, name="register"),
    path('adduser/',addUser, name="addUser"),
    path('modalform/', modelform, name="form"),
    path('addmodalform',addModalForm,name="modalform"),
]
