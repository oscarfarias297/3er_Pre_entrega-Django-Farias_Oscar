from django.shortcuts import render, redirect, get_object_or_404
from medicos.models import Medicos
from medicos.forms import MedicosForm


def index(request):
    return render(request, "medicos/index.html")

def medicos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Medicos.objects.filter(nombre__icontains=busqueda) | Medicos.objects.filter(apellido__icontains = busqueda)
    else:
        consulta = Medicos.objects.all()
    contexto = {"medicos":consulta}
    return render(request,"medicos/medicos_list.html", contexto)





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


def medicos_create(request):
    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("medicos:medicos_list")
    else:  # GET
        form = MedicosForm()
    return render(request, "medicos/medicos_form.html", {"form": form})

def medicos_update(request,pk):
    consulta = Medicos.objects.get(id=pk)
    if request.method == "POST":
        form = MedicosForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("medicos:medicos_list")
    else:  # GET
        form = MedicosForm(instance=consulta)
    return render(request, "medicos/medicos_form.html", {"form": form})


def confirmar_eliminar(request, pk: int):
    consulta = get_object_or_404(Medicos, id=pk)
    if request.method == "GET":
        consulta.delete()
        return redirect("medicos:medicos_list")
    return render(request, "medicos/medicos_confirm_delete.html", {"object": consulta})


