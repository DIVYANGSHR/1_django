from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index),
    path ('about/',views.about),
    path('about2/',views.about ,name='about')
]


