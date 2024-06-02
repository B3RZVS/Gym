from django.db import models
from ejercicio.models import Ejercicio

class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()

# Create your models here.
class Actividad(models.Model, ModeloBase):
    tiempoDescanso= models.DurationField()
    ejercicio= models.ForeignKey(Ejercicio, on_delete= models.CASCADE)

class Serie(models.Model, ModeloBase):
    secuencia= models.IntegerField()
    peso= models.FloatField()
    tiempo= models.DurationField()    
    repeticion= models.IntegerField()
    actividad= models.ForeignKey(Actividad, on_delete=models.CASCADE)

    def __str__ (self): #To_string
        return self.secuenciaS

#quedar hacer la clase de historial actividad, pero primero hay que hacer la del alumno.
 