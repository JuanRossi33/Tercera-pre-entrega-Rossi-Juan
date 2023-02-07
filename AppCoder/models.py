from django.db import models

# Create your models here.


class Curso(models.Model):

    grado = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    materia = models.CharField(max_length=20)


