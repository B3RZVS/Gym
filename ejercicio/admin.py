from django.contrib import admin
from .models import Ejercicio, EjercicioMusculo, Musculo, Categoria

admin.site.register (Categoria)
admin.site.register (Musculo)
admin.site.register (Ejercicio)
admin.site.register (EjercicioMusculo)

