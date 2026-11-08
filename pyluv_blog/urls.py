from . import views
from django.urls import path
from django.urls import include, re_path
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10], template_name="pyluv_blog/home.html")),
    re_path(r'^post/(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name="pyluv_blog/post.html")),
]