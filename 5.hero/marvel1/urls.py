from django.urls import path
from marvel1 import views

urlpatterns = [
      path('spiderman/',views.spiderman),
      path('superman/',views.ironman)
    ]
