from django.urls import path
from . import views
from pyluv_api.smsclassifiermodel import smsclassifier

urlpatterns = [
    path('', views.home, name="pyluv-api-home"),
    path('sms/id', views.sms_id, name="pyluv-api-sms-id"),
    path('sms/id/classify', smsclassifier.classify_text, name="pyluv-api-sms-id-classify"),
]