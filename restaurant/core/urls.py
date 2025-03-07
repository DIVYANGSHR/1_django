from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('product_detail/',views.product_detail,name='productdetail')
]