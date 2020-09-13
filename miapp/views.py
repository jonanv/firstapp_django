from django.shortcuts import render, HttpResponse, redirect

# Importacion de modelos
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

# Menu que es cargado en la vista contacto
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

# Metoto de la vista index
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

# Metodo de la vista hola-mundo
def hola_mundo(request):
    return render(request, 'hola_mundo.html')

# Metodo de la vista pagina
def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/inicio/')

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

# Metodo de las vista contacto
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

# Metodo save article
def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        response = HttpResponse(f"Articulo creado: { articulo.title } - { articulo.content }")
    else:
        response = HttpResponse("<h2>No se ha podido crear el articulo</h2>")

    return response

# Metodo create article
def create_article(request):
    return render(request, 'create_article.html')

# Metodo de la vista create full article
def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            articulo.save()

            # Crear mensajes flash (Sesion que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo: { articulo.id }')

            # return HttpResponse(title + ' ' + content + ' ' + public)
            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })

# Metodo de la vista articulo
def articulo(request):
    try:
        articulo = Article.objects.get(pk=6)
        # articulo = Article.objects.get(title="Superman", public=True)
        response = f"</br>Articulo: </br> Id: { articulo.id } - { articulo.title }"
    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)

# Metodo de la vista editar articulo
def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Batman dark night"
    articulo.public = True
    articulo.save()

    return HttpResponse(f"Articulo editado: { articulo.title } - { articulo.content }")

# Metodo de la vista articulos
def articulos(request):
    articulos = Article.objects.all()

    # order by
    # articulos = Article.objects.order_by('title')
    # articulos = Article.objects.order_by('-title')
    # articulos = Article.objects.order_by('id')[:3]
    # articulos = Article.objects.order_by('id')[3:10]
    # articulos = Article.objects.order_by('-id')
    
    # filters
    # articulos = Article.objects.filter(title='Batman')

    # lookups
    # articulos = Article.objects.filter(title__contains='articulo')
    # articulos = Article.objects.filter(title__exact='articulo')
    # articulos = Article.objects.filter(title__iexact='batman')

    # exclude
    # articulos = Article.objects.filter(title='prueba').exclude(public=False)

    # consulta SQL
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='prueba' AND public=0")

    # OR
    # articulos = Article.objects.filter(
    #     Q(title__contains='3') | Q(title__contains='prueba')
    # )

    articulos = Article.objects.filter(public=True).order_by('-id')

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

# Metodo de la vista eliminar articulo
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')