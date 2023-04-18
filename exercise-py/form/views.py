from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'form/home.html')


def form(request):
    return render(request, 'form/form.html')


def forms(request):
    return render(request, 'form/forms.html')


def formsucessfully(request):
    return render(request, 'form/formsucessfully.html')


def error(request):
    return render(request, 'form/error.html')
