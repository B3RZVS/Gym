from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
#from django.contrib.auth.hashers import make_password, check_password


class ModeloBase:
    def cambioEstado(self):
        self.activo = not self.activo
        self.save()
    def comprobacionCampos(campos,request):  
        for campo in campos:
            if not campo in request.data:
                raise ValidationError({"error": f"Falta el campo: {campo}"})
            
class Role(models.Model):
    ROLE_CHOICES = (
        ('profesor', 'Profesor'),
        ('alumno', 'Alumno'),
    )
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name
 
class Usuario(models.Model, ModeloBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    nombre= models.CharField(max_length=20,null= True)
    apellido= models.CharField(max_length=20, null= True)
    email= models.EmailField(null= True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, default= 2 , null=True, related_name='users')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
