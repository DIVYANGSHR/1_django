from django.shortcuts import render

# Create your views here.
def vilian(request):
    # context={'villian':'zola'}
    return render(request,'core/index.html',{'villian':'redskull'})


def hero(request):
    return render(request,'core/hero.html',{'hero':['SAUTH INDIAN ','ironman','UNIQNAME','thor','','black widow','hulk']})
