from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import categoria,subir_proyecto,usuariocliente,proyecto,proyecto_categoria

# Create your views here.
def inicio(request):
    return render(request,'index.html')


def proyectos(request):
    return render(request, 'proyectos.html')


def Contactos(request):
    return render(request, 'contactos.html')

def subirprojec(request):
    if request.method == 'POST':
        campo1 =request.POST.get('nombre')
        campo3 =request.POST.get('descripcion-de-proyecto')
        campo4 =request.POST.get('inversion-proyecto')
        campo5 =request.POST.get('repositorio')
        campo6 =request.POST.get('archivo-proyecto')

        mi_objeto=subir_proyecto(campo1=nombre, campo3=descripcion-de-proyecto, campo4=inversion-proyecto, campo5=repositorio, campo6=archivo-proyecto)

        mi_objeto.save()

    return render(request, 'subir-proyecto.html',{'success': True})
    
def signup(request):
    return render(request, 'signup.html')

def registro(request):
    return render(request, 'registro.html')
def carrito(request):
    return render(request, 'carrito.html')

