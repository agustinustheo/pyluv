from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'pyluv_blog/home.html', {'data':['Hello there dear visitors! Welcome to my humble blog app', 'Feel free to make yourselves at home']})