from django.shortcuts import render
from .forms import MarvelForms

# Create your views here.
def index (request):
    mf =MarvelForms()
    return render (request,"core/index.html" ,{'mf':mf})
