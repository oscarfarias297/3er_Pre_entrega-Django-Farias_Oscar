from django.shortcuts import render, redirect, get_object_or_404
from medicos.models import Medicos
from medicos.forms import MedicosForm


def index(request):
    return render(request, "medicos/index.html")

def medicos_list(request):
    consulta = Medicos.objects.all()
    contexto = {"medicos":consulta}
    return render(request,"medicos/medicos_list.html", contexto)

def confirmar_eliminar(request, pk: int):
    consulta = Medicos.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("medicos:medicos_list")
    return render(request, "medicos/medicos_confirmar_eliminar.html", {"object": consulta})



def medicos_modificar(request, medico_id=None):
    if medico_id:
        medico = get_object_or_404(Medicos, pk=medico_id)
    else:
        medico = None
    if request.method == "POST":
        form = MedicosForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect("medicos:medicos_list")
    else:
        form = MedicosForm(instance=medico)
        return render(request, "medicos/medicos_form.html", {"form": form})


def medicos_create(request, pk):
    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("medicos:medicos_list")
    else:  # GET
        form = MedicosForm()
    return render(request, "medicos/medicos_form.html", {"form": form})