from django.http import HttpResponse
import datetime
from django.template import Context, Template
from polls.models import Pagadores
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

pagador=Pagadores()
class PagadorForm(ModelForm):
    class Meta:
        model = Pagadores
        fields = ['logo_base64', 'pagador', 'tipo_cambio']

def index(request, template_name='polls/index.html'):
    pagador = Pagadores.objects.all().order_by('pk')
    data = {}
    data['object_list'] = pagador
    return render(request, template_name, data)

def pagadores_list(request, template_name='polls/pagadores.html'):
    pagador = Pagadores.objects.all()
    data = {}
    data['object_list'] = pagador
    return render(request, template_name, data)

def pagador_view(request, pk, template_name='polls/pagador_detail.html'):
    pagador= get_object_or_404(Pagadores, pk=pk)    
    return render(request, template_name, {'object':pagador})

def pagador_create(request, template_name='polls/pagador_form.html'):
    form = PagadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagadores')
    return render(request, template_name, {'form':form})

def pagador_update(request, pk, template_name='polls/pagador_form.html'):
    pagador= get_object_or_404(Pagadores, pk=pk)
    form = PagadorForm(request.POST or None, instance=pagador)
    if form.is_valid():
        form.save()
        return redirect('pagadores')
    return render(request, template_name, {'form':form})

def pagador_delete(request, pk, template_name='polss/pagador_confirm_delete.html'):
    pagador= get_object_or_404(Pagadores, pk=pk)    
    if request.method=='POST':
        pagador.delete()
        return redirect('pagadores')
    return render(request, template_name, {'object':pagador})

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
    if edad > year:
        palabra = 'tenías'
    else:
        palabra = 'tendrás'
    doc="<h1>en el año: %s %s %s años</h1>" %(year, palabra, edadFutura)
    return HttpResponse(doc)
