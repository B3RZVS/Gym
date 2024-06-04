from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    ROLE_CHOICES = (
        ('profesor', 'Profesor'),
        ('alumno', 'Alumno'),
    )
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

'''
class User(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
'''
    
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=20,null= True)
    apellido= models.CharField(max_length=20, null= True)
    email= models.EmailField(null= True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')
    def __str__(self):
        return self.nombre