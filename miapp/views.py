from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Anios hasta el 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if (year % 2 == 0):
            html += f"<li>{ str(year) }</li>"
        year += 1
    
    html += "</ul>"
    return HttpResponse(html)

def holaMundo(request):
    return HttpResponse("""
        <h1>Hola mundo con Django!</h1>
    """)

def pagina(request):
    return HttpResponse("""
        <h1>Pagina de mi web</h1>
        <p>Creado por Giovanni Vargas</p>
    """)