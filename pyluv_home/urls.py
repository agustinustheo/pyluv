from . import views
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    path('', views.home, name="pyluv-home"),
]