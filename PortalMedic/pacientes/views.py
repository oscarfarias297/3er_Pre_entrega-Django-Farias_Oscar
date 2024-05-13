from django.shortcuts import render

from pacientes.models import Paciente


def index(request):
    return render(request, "pacientes/index.html"),

def pacientes_list(request):
    consulta = Paciente.objects.all()
    contexto = {"pacientes":consulta}
    return render(request,"pacientes/pacientes_list.html", contexto)