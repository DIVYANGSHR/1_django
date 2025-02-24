from django.shortcuts import render
from . forms import MarvelForm

def index (request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            print(mf.cleaned_data['name'])
            print(mf.changed_data['password'])
            print(mf.cleaned_data['confirm_password'])
            mf =MarvelForm()

    else:
        mf= MarvelForm()
    return render (request,'core/index.html',{'mf':mf})




