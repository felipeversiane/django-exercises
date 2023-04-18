from django.urls import path
from form.views import home
from form.views import form
from form.views import forms
from form.views import formsucessfully

urlpatterns = [
    path('',    home),
    path('form/', form),
    path('forms/', forms),
    path('formsucessfully/', formsucessfully),
]