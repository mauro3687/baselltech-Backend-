from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def inicio(request):
    return render(request,'index.html')


def proyectos(request):
    return render(request, 'proyectos.html')


def Contactos(request):
    return render(request, 'contactos.html')

def subirprojec(request):
    return render(request, 'subir-proyecto.html')
    
def signup(request):
    return render(request, 'signup.html')
def registro(request):
    return render(request, 'registro.html')

