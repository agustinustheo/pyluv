from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('<h1>Oh Hello There, Welcome to Pyluv API</h1>')