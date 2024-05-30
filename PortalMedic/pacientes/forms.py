from django import forms
from .models import HistoriaClinica


from . import models

class PacientesForm(forms.ModelForm):
    
    class Meta:
        model = models.Paciente
        fields = ["nombre","apellido","DNI","fecha_nacimiento","telefono","obraSocial","numeroAfiliado","medico_tratante"]

    
class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['contenido']