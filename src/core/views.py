from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse('Hola desde Django!')


def saludar_con_etiqueta(request):
    return HttpResponse('<h1> Hola ! </h1>')


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f'{apellido}, {nombre}')


def index(request):
    context = {'año': 2024}
    return render(request, 'core/index.html', context)


def tirar_dados(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f'Has tirado el Dado y has sacado ¡{tiro_de_dado}! Ganaste '
    else:
        mensaje = f'Has tirado el Dado y has sacado ¡{tiro_de_dado}! Perdiste '

    datos = {
        'title': 'Tiro de Dados',
        'mensaje': mensaje,
        'fecha': datetime.now()
    }
    return render(request, 'core/dados.html', context=datos)

def ejercicio1 (request):
    #nombre = input("Ingrese Nombre: ")
    #apellido = input("Ingrese Apellido: ")
    nombre = "Acá había un input"
    apellido = "Acá También"

    datos = {
        'title': 'Ejercicio',
        'nombre': nombre,
        'apellido': apellido
    }
    return render(request, 'core/ejercicio1.html', context=datos)

def mostrar_notas(request):
    lista_de_notas = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'core/notas.html', {'notas': lista_de_notas})

def ejercicio_2(request):
    datos = [ {'nombre': 'juan', 'email': 'juan@django'},
             {'nombre': 'santi', 'email': 'santi@django'},
             {'nombre': 'agustín', 'email': 'agus@django'}, ]
    
    return render(request, 'core/respondiendo_template.html', {'usuarios': datos})
