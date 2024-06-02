from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    TIPOS = [
        ['1', 'Carta'],
        ['2', 'Catalogo'],
        ['3', 'Marketplace']
    ]

    nombre = models.CharField(max_length=100, unique=True)
    red_wifi = models.CharField(max_length=50, blank=True, null=True)
    clave_wifi = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPOS, default='1')
    telefono = models.CharField(max_length=50, blank=True, null=True)
    anuncio = models.FileField(upload_to='anuncios/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def get_tema_actual(self):
        tema = self.tema_empresa.last().tema
        return tema
    
    @property
    def planes(self):
        planes_empresa = self.plan_empresa.all()
        planes = list(map(lambda plan: plan.tipo, planes_empresa))

        return planes
    
class Rubro(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='rubros')
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class EmpresaRubro(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_rubro')
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE, related_name='rubro_empresa')
    video_intro = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.empresa.nombre + ' - ' + self.rubro.nombre
    
class Plan(models.Model):
    TIPOS = (
        ('1', 'e-commerce-wpp'),
        ('2', 'pedidos'), 
        ('3', 'stock'),
    )

    tipo = models.CharField(max_length=50, choices=TIPOS, default='1')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='plan_empresa')
        
    
class UserEmpresa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_empresa')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_user')

    def __str__(self):
        return self.user.username + ' - ' + self.empresa.nombre