from django.contrib import admin
from django.urls import path, include
from .views import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orderapp.urls')),
] 

handler404 = 'galetos.views.handler404'