from django.db import models
from rest_framework.exceptions import ValidationError

# Create your models here.
class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()
    def comprobacionCampos(campos,request):  
        for campo in campos:
            if not campo in request.data:
                raise ValidationError({"error": f"Falta el campo: {campo}"})

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
        null=True,
        blank=True)
    
    '''
    imagen = models.ImageField(
        "upload_to='ejercicios/'", 
        null=True,
        blank=True)
    '''
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ejercicios')
    
    activo= models.BooleanField(default=True)
    def __str__ (self): #To_string
        return f"{self.nombre} - ({self.categoria.nombre})"
    
    '''
    def asignarRubros(self,r):
        log = []
        for rubro_id in r:
            try:
                rubro= Rubro.objects.get(id=rubro_id)
            except Rubro.DoesNotExist:
                log.append({"Rubro":f"Rubro con id {rubro_id} no existe"})
            
            detalle = DetalleRubro (
                rubro = rubro,
                persona = self
            )
            detalle.save()
            log.append({"Rubro":f"Rubro con id {rubro_id} asignado"})

        return log
    '''


class EjercicioMusculo (models.Model, ModeloBase):
    ejercicio= models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name="detalles")    
    musculo= models.ForeignKey(Musculo, on_delete=models.CASCADE, related_name="detalles")
    
    def __str__(self):
        return f"{self.ejercicio.nombre} ({self.ejercicio.categoria.nombre}) - {self.musculo.nombre}"