from . import views
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10], template_name="pyluv_blog/home.html")),
    url(r'^post/(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name="pyluv_blog/post.html")),
]