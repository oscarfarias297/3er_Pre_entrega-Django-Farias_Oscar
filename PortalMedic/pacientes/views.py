from django.shortcuts import render, redirect, get_object_or_404

from pacientes.models import Paciente, HistoriaClinica
from pacientes.forms import PacientesForm, HistoriaClinicaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "pacientes/index.html")


@login_required
def pacientes_list(request):
    query = request.GET.get('busqueda', '')
    if query:
        pacientes = Paciente.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(DNI__icontains=query)
        )
    else:
        pacientes = Paciente.objects.all()
    return render(request, 'pacientes/pacientes_list.html', {'pacientes': pacientes})


@login_required
def pacientes_create(request):
    if request.method == "POST":
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list")
    else:  # GET
        form = PacientesForm()
    return render(request, "pacientes/pacientes_form.html", {"form": form})


@login_required
def confirmar_eliminar(request, pk: int):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "GET":
        consulta.delete()
        return redirect("pacientes:pacientes_list")
    return render(request, "pacientes/pacientes_confirm_delete.html", {"object": consulta})

@login_required
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
    
@login_required
def pacientes_update(request,pk):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        form = PacientesForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list")
    else:
        form = PacientesForm(instance=consulta)
    return render(request, "pacientes/pacientes_form.html", {"form": form})

@login_required
def pacientes_delete(request,pk):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("pacientes:pacientes_list")
    return render (request, "pacientes/pacientes_confirm_delete.html",{"object":consulta})

@login_required
def guardar_historia(request, pk):
    paciente = get_object_or_404(Paciente, id=pk)
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia = form.save(commit=False)
            historia.paciente = paciente
            historia.save()
            return redirect("pacientes:ver_historia", pk=paciente.id)
    else:
        form = HistoriaClinicaForm()
    return render(request, 'pacientes/guardar_historia.html', {'form': form, 'paciente': paciente})


@login_required
def ver_historia(request, pk):
    paciente = get_object_or_404(Paciente, id=pk)
    historias = HistoriaClinica.objects.filter(paciente=paciente).order_by('-fecha_creacion')
    return render(request, 'pacientes/ver_historia.html', {'paciente': paciente, 'historias': historias})

@login_required
def modificar_hc(request,pk):
    historia = Paciente.objects.get(id=pk)
    if request.method == "GET":
        form = HistoriaClinicaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect("pacientes:pacientes_list", id = pk)
    else:
        form = HistoriaClinicaForm(instance=historia)
    return render(request, "pacientes/modificar_hc.html", {"form": form})