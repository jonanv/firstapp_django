from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def index(request):
    return HttpResponse("""
        <h1>Inicio</h1>
    """)

def holaMundo(request):
    return HttpResponse("""
        <h1>Hola mundo con Django!</h1>
    """)

def pagina(request):
    return HttpResponse("""
        <h1>Pagina de mi web</h1>
        <p>Creado por Giovanni Vargas</p>
    """)