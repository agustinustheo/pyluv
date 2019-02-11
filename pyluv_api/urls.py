from django.urls import path
from . import views
from pyluv_api.smsclassifiermodel import smsclassifier
from pyluv_api.fakenewsdetector import en_fakenewsdetector, id_fakenewsdetector
from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from pyluv_api.models import API

urlpatterns = [
    path('', ListView.as_view(queryset=API.objects.all().order_by("-date")[:10], template_name="pyluv_api/home.html")),
    path('sms/id', views.sms_id, name="pyluv-api-sms-id"),
    path('fakenews/en', views.fakenews_en, name="pyluv-api-fakenews-en"),
    path('fakenews/id', views.fakenews_id, name="pyluv-api-fakenews-id"),
    path('sms/id/classify', smsclassifier.classify_text, name="pyluv-api-sms-id-classify"),
    path('fakenews/en/classify', en_fakenewsdetector.checkNews, name="pyluv-api-sms-id-classify"),
    path('fakenews/id/classify', id_fakenewsdetector.checkNews, name="pyluv-api-sms-id-classify"),
    url(r'^(?P<base_url>\w+)/$', views.api_docs, name='pyluv-api-docs'),
]