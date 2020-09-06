from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
    <h1>Sitio web con Django | Giovanni</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

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
    return HttpResponse(layout + html)

def holaMundo(request):
    return HttpResponse(layout + """
        <h1>Hola mundo con Django!</h1>
    """)

def pagina(request):
    return HttpResponse(layout + """
        <h1>Pagina de mi web</h1>
        <p>Creado por Giovanni Vargas</p>
    """)

def contacto(request, nombre):
    return HttpResponse(layout + f"<h2>Contacto { nombre }</h2>")