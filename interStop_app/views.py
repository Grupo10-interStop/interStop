from django.http import HttpResponse
from django.shortcuts import render
#from interStop_app.forms import formulario_datos
from interStop_app.models import Departamento
from interStop_app.models import Municipio
from interStop_app.models import ProblemaDes
from interStop_app.models import Sector_afectado
from interStop_app.models import Problema
import datetime

# Create your views here.

def test(request):
    return render(request, "test/test.html")

def modelo(request):
    return render(request, "modelo.html")

def formulario(request):


    if request.method=="GET":

       """ dep=request.GETeps"]
        mun=request.GET["muni"]
        prob=request.GET["problms"]
        sec=request.GET["sect"]

        ubicacion_r=Ubicacion()
        ubicacion_r.id_ubicacion=1
        ubicacion_r.id_departamento=dep
        ubicacion_r.id_municipio=mun
        ubicacion_r.save()
"""
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    des_problemas = ProblemaDes.objects.all()
    sector_nombres = Sector_afectado.objects.all()
    return render(request, "formulario.html", {"departamentos":departamentos, "municipios": municipios,
    "des_problema": des_problemas, "sector_nombres": sector_nombres})



def enviar(request):
    
    mensaje = "%r"%request.GET["sect"]
    dep="%r"%request.GET["deps"]
    mun="%r"%request.GET["muni"]
    prob="%r"%request.GET["problms"]
    sec="%r"%request.GET["sect"]
    come="%r"%request.GET["comen"]
    fecha=datetime.date.today()
    
   # identificador=Problema.annotate(Count('id_pro'))    

    problemas=Problema()
    problemas.descripcion=come
    problemas.id_departamentop=dep
    problemas.id_municipiop=mun
    problemas.id_problemap=prob
    problemas.id_sectorp=sec
    problemas.id_usuariop=1
    problemas.fecha=fecha
    problemas.save()
    
    return HttpResponse(mensaje) 


