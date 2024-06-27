from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)




class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    