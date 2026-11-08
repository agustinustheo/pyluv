from . import views
from django.urls import path
from django.urls import include, re_path
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    path('', views.startpage, name="pyluv-startpage"),
    path('home', views.home, name="pyluv-home"),
]