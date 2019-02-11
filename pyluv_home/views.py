from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def startpage(request):
  return render(request, 'pyluv_home/startpage.html')

def home(request):
  return render(request, 'pyluv_home/home.html')