from django.shortcuts import render
from medicos.models import Medicos


def index(request):
    return render(request, "medicos/index.html")

def medicos_list(request):
    consulta = Medicos.objects.all()
    contexto = {"medicos":consulta}
    return render(request,"medicos/medicos_list.html", contexto)