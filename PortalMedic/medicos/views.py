from django.shortcuts import render, redirect, get_object_or_404
from medicos.models import Medicos
from medicos.forms import MedicosForm
from django.db.models import Q



def index(request):
    return render(request, "medicos/index.html")

def medicos_list(request):
    query = request.GET.get('busqueda', '')
    if query:
        medicos = Medicos.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(DNI__icontains=query)
        )
    else:
        medicos = Medicos.objects.all()
    return render(request, 'medicos/medicos_list.html', {'medicos': medicos})

def confirmar_eliminar(request, pk: int):
    consulta = Medicos.objects.get(id=pk)
    if request.method == "GET":
        consulta.delete()
        return redirect("medicos:medicos_list")
    return render(request, "medicos/medicos_confirm_delete.html", {"object": consulta})



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

def medicos_delete(request,pk):
    consulta = Medicos.objects.get(id=pk)
    if request.method == "GET":
        consulta.delete()
        return redirect("medicos:medicos_list")
    return render (request, "medicos/medicos_confirm_delete.html",{"object":consulta})