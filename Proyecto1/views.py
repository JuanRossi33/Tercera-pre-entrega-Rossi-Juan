from django.template import Template, Context
from django.http import HttpResponse


def saludo(request):

    return HttpResponse("Hola")

    

def prueba(request):

    html = open("C:/Users/Usuario/Desktop/Programación/Web/Proyecto1/Proyecto1/Plantilla/plantilla.html")

    plantilla = Template(html.read())

    html.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

    