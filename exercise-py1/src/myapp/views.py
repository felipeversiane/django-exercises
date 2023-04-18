# from django import get_version
# from django.views.generic import TemplateView
from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    data ="HOME"
    return HttpResponse(data)

def form(request):
    data ="FORM"
    return HttpResponse(data)

def forms(request):
    data ="FORMS"
    return HttpResponse(data)

def formsucessfuly(request):
    data = "FORMSUCESSFULL"
    return HttpResponse(data)