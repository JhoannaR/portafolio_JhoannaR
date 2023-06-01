from django.shortcuts import render
from .models import Project

def home(request):
    # para traer todos los objetos existentes en el modelo
    projects = Project.objects.all() 
    return render(request, 'home.html', {'projects':projects}) 