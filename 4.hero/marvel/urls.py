from django.urls import path
from marvel import views

urlpatterns = [
      path('spiderman/',views.spiderman),
      path('superman/',views.ironman)
      ]