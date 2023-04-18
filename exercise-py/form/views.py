# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    data = "home1"
    return HttpResponse(data)


def form(request):
    data = "form"
    return HttpResponse(data)


def forms(request):
    data = "forms"
    return HttpResponse(data)


def formsucessfully(request):
    data = "formsucess"
    return HttpResponse(data)
