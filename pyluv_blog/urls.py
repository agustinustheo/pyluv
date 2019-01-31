from . import views
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from pyluv_blog.models import Post

urlpatterns = [
    url('posts', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                            template_name="pyluv_blog/blog.html")),
    path('', views.home, name="pyluv-blog-home"),
    url(r'^post/(?P<pk>\d+)$', DetailView.as_view(model = Post,
                            template_name="pyluv_blog/post.html")),
]