from django.db import models

# Create your models here.


class Animal(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    
class persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    
class auto(models.Model):
    marca = models.CharField(max_length=15)
    velocidad = models.IntegerField()
    fecha_creacion = models.DateField()
    