from django.http import HttpResponse
import datetime
from django.template import Context, Template

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def index(request):
    p1=Persona("miro","torres")
    doc_externo = open("E:\DJangoWorkspace\\viamax\polls\\templates\polls\index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"persona": p1})
    doc = plt.render(ctx)
    return HttpResponse(doc)

def boton(request):
    return HttpResponse("<button onClick=(console.log('holas'))>Prueba</button>")

def date(request):
    date=datetime.datetime.now()
    doc="""
    <html>
    <body>
    <h1>Fecha de hoy: %s </h1>
    </body>
    </html>
    """ % date
    return HttpResponse(doc)   

def calcularEdad(request, edad, year):
    periodo=year-2019
    edadFutura=edad+periodo
    palabra=""
    if edad < year:
        palabra = 'tenías'
    else:
        palabra = 'tendrás'
    doc="<h1>en el año: %s %s %s años</h1>" %(year, palabra, edadFutura)
    return HttpResponse(doc)
