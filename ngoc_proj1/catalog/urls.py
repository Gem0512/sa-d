from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.catalog),
    path('product', views.product),
    path('index', views.index),
]
