from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('frame/', views.frame, name="frame"),
    path('glasses/', views.glasses, name="glasses"),
    path('update_item/', views.updateItem, name="checkout"),
]