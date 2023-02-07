from django.db import models

# Create your models here.

#Clase Modelo

class Curso(models.Model):    

    grado = models.IntegerField()

#Clase Estudiante

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

#Clase Profesor

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    materia = models.CharField(max_length=20)






