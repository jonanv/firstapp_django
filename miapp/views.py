from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def holaMundo(request):
    return HttpResponse("""
        <h1>
            Hola mundo con Django!
        </h1>
    """)