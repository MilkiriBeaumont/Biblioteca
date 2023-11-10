from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import proyecto
from django.contrib import messages
from models import Formproyecto


# Create your views here.

def display(request):
    return HttpResponse("<h1>hola mundo</h1>")

def template (request):
    return render (request, 'templatesApp/template.html')

def listadoProyecto(request):
    Proyecto = Proyecto.objects.all()
    data = {'Proyecto': Proyecto}
    return render(request, 'template.html', data)

def agregarProyecto(request):
    form = Formproyecto()
    if request.method == 'POST':
        form =  Formproyecto (request.POST)
    if form.is_vail():
        form.save()
        return template (request)
    data = {'form': form}
    return render(request,'agregarProyecto.html',data)