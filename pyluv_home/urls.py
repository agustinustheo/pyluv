from . import views
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    path('', views.startpage, name="pyluv-startpage"),
    path('home', views.home, name="pyluv-home"),
]