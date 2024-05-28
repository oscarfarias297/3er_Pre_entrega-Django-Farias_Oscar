from django.shortcuts import render, redirect, get_object_or_404

from pacientes.models import Paciente
from pacientes.forms import PacientesForm


def index(request):
    return render(request, "pacientes/index.html")

def pacientes_list(request):
    consulta = Paciente.objects.all()
    contexto = {"pacientes":consulta}
    return render(request,"pacientes/pacientes_list.html", contexto)

def pacientes_create(request):
    if request.method == "POST":
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list")
    else:  # GET
        form = PacientesForm()
    return render(request, "pacientes/pacientes_form.html", {"form": form})

def confirmar_eliminar(request, pk: int):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("pacientes:pacientes_list")
    return render(request, "pacientes/pacientes_confirm_delete.html", {"object": consulta})

def pacientes_modificar(request, medico_id=None):
    if medico_id:
        medico = get_object_or_404(Paciente, pk=medico_id)
    else:
        medico = None
    if request.method == "POST":
        form = PacientesForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list")
    else:
        form = PacientesForm(instance=medico)
        return render(request, "pacientes/pacientes_form.html", {"form": form})
    

def pacientes_update(request,pk):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        form = PacientesForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list")
    else:  # GET
        form = PacientesForm(instance=consulta)
    return render(request, "pacientes/pacientes_form.html", {"form": form})


def pacientes_delete(request,pk):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("pacientes:pacientes_list")
    return render (request, "pacientes/pacientes_confirm_delete.html",{"object":consulta})

def pacientes_hc(request,pk):
    consulta = Paciente.objects.get(id=pk)
    contexto = {"pacientes":consulta}
    return render(request,"pacientes/pacientes_hc.html", contexto)