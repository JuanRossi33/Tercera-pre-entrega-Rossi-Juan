from django.urls import path
from Proyecto1.views import *
from AppCoder.views import *


urlpatterns = [
    path('saludo/', saludo),
    path('test/', prueba),
    path('cursos/', curso, name="Curso"),
    path('estudiante/', student, name="Estudiante"),
    path('profesor/', professor, name="Profesor"),
    path('cursoFormulario/', cursoFormulario, name="Formulario"),
    path('busquedaDato/', busquedaDato, name="buscarDato"),
    path('buscar/', buscar, name="Buscar"),

    


    
]



