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
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")

    datos = {
        'title': 'Ejercicio',
        'nombre': nombre,
        'apellido': apellido
    }
    return render(request, 'core/ejercicio1.html', context=datos)
