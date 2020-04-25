from django.shortcuts import render, redirect
from .models import *
from apps.lista.models import Listado
from django.urls import reverse_lazy
from django.views.generic import *
from apps.lista.forms import ListadoForm
from django.http import *
from django.conf import settings
from io import BytesIO
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4, landscape, letter
#from reportlab.lib.units import inch, mm, cm
#from reportlab.lib.fonts import *
from django.views.generic import ListView
#from reportlab.lib import colors
#from reportlab.platypus import TableStyle, Table, Paragraph
from datetime import date
#from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)

#from reportlab.lib.enums import TA_CENTER

opc_icono = 'fa fa-address-card-o'
opc_ruta = '/matriculas/'
opc_nuevo = '/matriculas/nuevo'
opc_crud = '/matriculas/crear/'
opc_delete = '/matriculas/borrar'
opc_entidad = 'Matriculas'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
    }
    if request.method == 'GET':
        data['form'] = ListadoForm()
    return render(request, 'back-end/listado/listado_form.html', data)


def crear(request):
    f = ListadoForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    alumno = request.POST.get('alumno')
    periodo = request.POST.get('periodo')
    curso = request.POST.get('curso')
    if request.method == 'POST' and 'action' in request.POST:
        if Listado.objects.filter(alumno=alumno, curso=curso, periodo=periodo, estado=0):
            f = ListadoForm(request.POST)
            data = {
                'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
                'form': f, 'dupla': 'Ya existe un registro igual'
            }
        else:

            if f.is_valid():
                f.save()
                a = Alumno.objects.get(id=alumno)
                a.estado = 0
                a.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
                    'form': f
                }
                return render(request, 'back-end/listado/listado_form.html', data)
            return HttpResponseRedirect('/matriculas/lista')
        return render(request, 'back-end/listado/listado_form.html', data)

def Matriculas_lista(request):
    matriculas_list = Listado.objects.filter(estado=0)
    contexto = {'matriculas_list': matriculas_list}
    return render(request, "back-end/listado/listado.html", contexto)

