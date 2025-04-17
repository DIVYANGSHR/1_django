from django.shortcuts import render
from . models import  Cake


# Create your views here.
def index (request):
    return render(request,"core/index.html" )

def about (request):
    return render(request,'core/about.html')

# def cake_bakery(request):
#     cb = Cake.objects
