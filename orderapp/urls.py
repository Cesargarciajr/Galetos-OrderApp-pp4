from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('neworder/', views.new_order, name="neworder"),
    path('orderslist/', views.orders_list, name="orderslist"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('accounts/', include('allauth.urls')),
]
