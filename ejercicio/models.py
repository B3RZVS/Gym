from django.db import models

# Create your models here.
class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()

class Categoria (models.Model, ModeloBase):
    nombre= models.CharField(
        max_length=50,
        null=False)
    
    activo= models.BooleanField(default=True)

    def __str__ (self): #To_string
        return self.nombre

class Musculo (models.Model, ModeloBase):
    nombre= models.CharField(
        max_length=50,
        null=False)
    activo= models.BooleanField(default=True)

    def __str__ (self): #To_string
        return self.nombre
    
class Ejercicio (models.Model, ModeloBase):
    nombre= models.CharField(
        max_length=50,
        null=False)
    
    descripcion=models.CharField(
        max_length=100,
        null=False)
    
    imagen = models.ImageField(
        "upload_to='ejercicios/'", 
        null=True,
        blank=True)

    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null=True)
    
    activo= models.BooleanField(default=True)
    def __str__ (self): #To_string
        return self.nombre

class EjercicioMusculo (models.Model, ModeloBase):
    ejercicio= models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name="detalles")    
    musculo= models.ForeignKey(Musculo, on_delete=models.CASCADE, related_name="detalles")
    
    def __str__(self):
        return f"{self.ejercicio.nombre} - {self.musculo.nombre}"