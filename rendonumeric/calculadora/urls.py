from django.urls import path, include
from calculadora import views as vistas

urlpatterns = [
    path('',vistas.home, name='home'),

]