from django.db import models
from ejercicio.models import Ejercicio
from rest_framework.exceptions import ValidationError

class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()

    def comprobacionCampos(campos,request):  
        for campo in campos:
            if not campo in request.data:
                raise ValidationError({"error": f"Falta el campo: {campo}"})

# Create your models here.
class Actividad(models.Model, ModeloBase):
    tiempoDescanso= models.DurationField()
    ejercicio= models.ForeignKey(Ejercicio, on_delete= models.CASCADE, null=True ,related_name='actividades')
    activo= models.BooleanField(default=True)


class Serie(models.Model, ModeloBase):
    secuencia= models.IntegerField()
    peso= models.FloatField()
    tiempo= models.DurationField()    
    repeticion= models.IntegerField()
    actividad= models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name= 'series')
    activo= models.BooleanField(default=True)
    
    def __str__ (self): #To_string
        return self.secuenciaS

#quedar hacer la clase de historial actividad, pero primero hay que hacer la del alumno.
 