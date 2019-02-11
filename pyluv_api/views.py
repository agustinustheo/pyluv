from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from pyluv_api.models import API, APIUrl

# Create your views here.

def api_docs(request, base_url):
  api_details = get_object_or_404(API, base_url=base_url+'/')
  api_url = APIUrl.objects.filter(base_api=api_details)
  return render_to_response('pyluv_api/api_docs.html', {'api' : api_details, 'api_url' : api_url})

def sms_id(request):
  return render(request, 'pyluv_api/indonesian_sms_classify.html')

def fakenews_en(request):
  return render(request, 'pyluv_api/en_fake_news_detector.html')

def fakenews_id(request):
  return render(request, 'pyluv_api/id_fake_news_detector.html')