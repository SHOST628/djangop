from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 1、define view method
# 2、config url, mapping url and view


# purpose :http://localhost:8000/index
def index(request):
    return HttpResponse('Welcome...')


def index2(request):
    return HttpResponse('hello world!')