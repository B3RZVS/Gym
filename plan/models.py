from django.db import models
from django.utils import timezone
from actividad.models import Actividad

# Create your models here.
class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()

class Plan(models.Model, ModeloBase):
    nombre = models.CharField(max_length=60)
    fechaInicio= models.DateTimeField(default=timezone.now)
    fechaInicio= models.DateTimeField()
    #creador= models.ForeignKey(Usuario, related_name='planes')
    
    def __str__ (self): #To_string
        return self.nombre

class DiaPlan(models.Model, ModeloBase):
    DIAS=(
        ('1','Lunes'),
        ('2','Martes'),
        ('3','Miercoles'),
        ('4','Jueves'),
        ('5','Viernes'),
        ('6','Sabado'),
        ('7','Domingo'),
    )
    dia= models.CharField(max_length=20,choices=DIAS,default='1')
    plan= models.ForeignKey(Plan, on_delete= models.CASCADE,related_name='dias_plan')

    def __str__ (self): #To_string
        return self.dia
    
class ActividadesPorDia (models.Model, ModeloBase):

    dia=models.ForeignKey(DiaPlan,on_delete= models.CASCADE,related_name='dia_actividad')
    actividad= models.ForeignKey(Actividad, on_delete= models.CASCADE,related_name='actividad_dia')

    def __str__(self):
        return f"{self.dia.dia} - {self.actividad.ejercicio}"
    
#agregar alumnoPlan