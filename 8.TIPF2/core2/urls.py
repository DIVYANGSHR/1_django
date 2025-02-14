from django.urls import path
from core2 import views

urlpatterns = [
      path('',views.index),
      path('about/',views.about)
      ]
