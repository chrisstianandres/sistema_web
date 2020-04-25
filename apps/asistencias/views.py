from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
#import pandas as pd
from .models import *
from apps.horario.models import *
from apps.asistencias.forms import *
from apps.asistencias.models import Asistencias
import json
from django.http import *

def vista_asistencias(request):
    form = AsistenciasForm()
    if request.method == 'POST':
        form = AsistenciasForm(request.POST)
    return render(request, 'back-end/asistencia/asistencias_form.html', {'form': form})

def get_asistencias(request):
    response = {"resp": 'False'}
    return HttpResponse(json.dumps(response), content_type="application/json")

def save_asistencia(request):
    data = {}
    fecha_hoy = date.today()
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
           if Asistencias.objects.filter(Horario_id=sub['horario'], Listado_id=sub['listado'], fecha=fecha_hoy):
               data['resp'] = False
           else:
               h = Horario.objects.get(pk=sub['horario'])
               h.asist_alum = 2
               h.save()
               n = Asistencias()
               n.Horario_id = sub['horario']
               n.Listado_id = sub['listado']
               n.fecha = fecha_hoy
               n.Asistencia = sub['asistencia']
               n.save()
               data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")