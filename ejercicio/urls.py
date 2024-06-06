from django.contrib import admin
from django.urls import path
from .views import MusculoAbm, CategoriaAbm, EjercicioAbm, EjercicioMusculoAbm

urlpatterns = [
    path('musculo/', MusculoAbm.as_view(), name='musculo'),
    path('categoria/', CategoriaAbm.as_view(), name='categoria'),
    path('ejercicio/', EjercicioMusculoAbm.as_view(), name='ejercicio'),
    path('ejercicioMusculo/', EjercicioMusculoAbm.as_view(), name='ejercicioMusculo'),
]