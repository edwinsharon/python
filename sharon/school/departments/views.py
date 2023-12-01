from django.shortcuts import render
from django.http import Httpresponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>this is homepage<h1>')
    