from django.contrib import admin
from django.urls import path , include
from home import views
urlpatterns = [
    
    path("",views.index, name="home"),
    path("contacts",views.contacts, name="contacts"),
    path("about",views.about, name="about"),
    path("softy",views.softy, name="softy"),
]