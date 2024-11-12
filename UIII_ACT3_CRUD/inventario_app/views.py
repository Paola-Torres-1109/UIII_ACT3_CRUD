from django.shortcuts import render
from .models import Inventario
# Create your views here.

def inicio_vista(request):
    loscarros=Inventario.objects.all

    return render(request,"gestionarInventario.html", {"miscarros":loscarros})

def registrarInventario(request):
    id_inventario=request.POST["txtcodigo"]
    vehiculo=request.POST["txtvehiculo"]
    cantidad_auto=request.POST["numcantidad_a"]
    ubicacion=request.POST["txtubicacion"]
    estado_bmr=request.POST["txtestado"]
    proveedor=request.POST["txtproveedor"]
    guardarinventario=Inventario.objects.create(id_inventario=id_inventario, vehiculo=vehiculo, cantidad_auto=cantidad_auto, ubicacion=ubicacion, estado_bmr=estado_bmr, proveedor=proveedor)
    return redirect("/")

def seleccionarInventario(request,id_inventario):
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    return render(request, "editarInventario.html", {"miscarros": inventario})

def editarInventario(request):
    id_inventario=request.POST["txtcodigo"]
    vehiculo=request.POST["txtvehiculo"]
    cantidad_auto=request.POST["numcantidad_a"]
    ubicacion=request.POST["txtubicacion"]
    estado_bmr=request.POST["txtestado"]
    proveedor=request.POST["txtproveedor"]
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    inventario.id_inventario=id_inventario
    inventario.vehiculo=vehiculo
    inventario.cantidad_auto=cantidad_auto
    inventario.ubicacion=ubicacion
    inventario.estado_bmr=estado_bmr
    inventario.proveedor=proveedor
    inventario.save()
    return redirect("/")

def borrarInventario(request, id_inventario):
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()

    return redirect("/")