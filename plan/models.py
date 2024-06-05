from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from actividad.models import Actividad
from usuario.models import Usuario

# Create your models here.
class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()

    def comprobacionCampos(campos,request):  
        for campo in campos:
            if not campo in request.data:
                raise ValidationError({"error": f"Falta el campo: {campo}"})

class Plan(models.Model, ModeloBase):
    nombre = models.CharField(max_length=60)
    fechaInicio= models.DateTimeField(default=timezone.now)
    fechaFin= models.DateTimeField(null=True,blank=True)
    creador= models.ForeignKey(Usuario, on_delete= models.CASCADE,null= True ,related_name='planes')
    activo= models.BooleanField(default= True)
    
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
    activo= models.BooleanField(default= True)
    def __str__ (self): #To_string
        return self.dia
    
    def asignarActividad(self,actividades):
        act_totales=[]

        for actividad in actividades:
            try:
                    actividad= Actividad.objects.get(id=actividad)
            except Actividad.DoesNotExist:
                    raise ValidationError({"error": f"La '{actividad}' no existe"})
            
            if not ActividadesPorDia.objects.filter(dia=self, actividad= actividad).exists():

                aux = ActividadesPorDia.objects.create(
                        dia=self,
                        actividad=actividad
                    )
                act_totales.append(aux)
                
            else:
                raise ValidationError({"error": f"La '{actividad}' ya esta en el plan"})

        return aux
    
    
class ActividadesPorDia (models.Model, ModeloBase):

    dia=models.ForeignKey(DiaPlan,on_delete= models.CASCADE,related_name='dia_actividad')
    actividad= models.ForeignKey(Actividad, on_delete= models.CASCADE,related_name='actividad_dia')

    def __str__(self):
        return f"{self.dia.dia} - {self.actividad.ejercicio}"
    
class AlumnoPlan(models.Model, ModeloBase):

    alumno= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='planes_asociados')
    plan= models.ForeignKey(Plan, on_delete= models.CASCADE, related_name='alumnos')

    def __str__ (self): #To_string
        return f"{self.alumno.nombre} {self.plan.nombre}"
