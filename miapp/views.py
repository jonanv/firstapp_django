from django.shortcuts import render, HttpResponse, redirect

# Importacion de modelos
from miapp.models import Article

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
            <a href="/pagina">Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    html = ""
    year = 2021
    hasta = range(year, 2050)
    # while year <= 2050:
    #     if (year % 2 == 0):
    #         html += f"<li>{ str(year) }</li>"
    #     year += 1

    nombre = 'Giovanni Vargas'
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']
    # lenguajes = []
    
    return render(request, 'index.html', {
        'title': 'Inicio prueba',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/inicio/')

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "El nombre completo es: "
        html += f"<h3>{ nombre } { apellidos }</h3>"

    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)

# Metodo de la vista Crear articulo
def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado: { articulo.title } - { articulo.content }")