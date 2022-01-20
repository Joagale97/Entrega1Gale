from django.http import request
from django.shortcuts import render, redirect
from . models import Celulares

# Create your views here.
def home(request):
    celularesListados= Celulares.objects.all()


    return render(request, "gestionCelulares.html" , {"celulares": celularesListados})

def registarcompra(request):
    marca=request.POST['txtMarca']
    modelo=request.POST['txtModelo']
    sistema_operativo=request.POST['txtSistema']
    memoria_en_GB=request.POST['numMemoria']
    compañia=request.POST['txtCompañia']
    cantidad=request.POST['numCantidad']
    
    celulares=Celulares.objects.create(marca=marca, modelo=modelo, sistema_operativo=sistema_operativo,memoria_en_GB=memoria_en_GB, compañia=compañia , cantidad= cantidad)
    return redirect ('/')





def eliminar_celulares(request, id):
    celulares = Celulares.objects.get(id=id)
    celulares.delete()

    return redirect('/')





def edicionCelular(request,id):
    celular= Celulares.objects.get(id=id)

    return render(request,"edicionCelular.html", {"celular": celular})

def editarcompra(request):
    id=request.POST['id']
    marca=request.POST['txtMarca']
    modelo=request.POST['txtModelo']
    sistema_operativo=request.POST['txtSistema']
    memoria_en_GB=request.POST['numMemoria']
    compañia=request.POST['txtCompañia']
    cantidad=request.POST['numCantidad']
    
    
    celulares = Celulares.objects.get(id=id)

    celulares.marca= marca
    celulares.modelo= modelo
    celulares.sistema_operativo= sistema_operativo
    celulares.memoria_en_GB= memoria_en_GB
    celulares.compañia= compañia
    celulares.cantidad= cantidad

    celulares.save()

    return redirect('/')


