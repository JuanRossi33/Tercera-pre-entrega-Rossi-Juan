from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario

# Create your views here.


def curso(request):
    
    Curso1 = Curso(grado=4)
    Curso1.save()

    return HttpResponse(f"El curso que he creado es: {Curso1.grado}") 


def student(request):
    

    return render(request,"AppCoder/estudiante.html")



def professor(request):
    

    return render(request,"AppCoder/profesor.html")


def cursoFormulario(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data
            curso = Curso(grado=info["grado"])
            curso.save()

            return render(request, "AppCoder/cursos.html")

    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})


def busquedaDato(request):

    return render(request, "AppCoder/busquedaDato.html")

def buscar(request):

    if request.GET['grado']:

        grado = request.GET['grado']
        cursos = Curso.objects.filter(grado__icontains=grado)

        return render(request, "AppCoder/resultados.html", {"cursos":cursos, "grado":grado})

    else:

        respuesta = "No hay datos. "
    
    
    return HttpResponse(respuesta)










    



