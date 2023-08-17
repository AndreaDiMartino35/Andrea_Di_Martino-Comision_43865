from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.email}"
    
class Criadero(models.Model):
    nombre=models.CharField(max_length=50)
    cuit=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} - ({self.cuit}) - ({self.email})"
    
class Tambo(models.Model):
    nombre=models.CharField(max_length=50)
    cuit=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} - ({self.cuit}) - ({self.email})"
    
class Agricultor(models.Model):
    nombre=models.CharField(max_length=50)
    cuit=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} - ({self.cuit}) - ({self.email})"
    
class Foto(models.Model):
    imagen = models.ImageField(upload_to="imagenes")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"