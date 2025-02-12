from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about (request):
    return HttpResponse('<h1> This is my dairy </h1>')
def contact (request):
    return HttpResponse('<h1> This is your dairy </h1>')
