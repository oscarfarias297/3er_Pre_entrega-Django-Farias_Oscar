from django import forms

from . import models

class PacientesForm(forms.ModelForm):
    
    class Meta:
        model = models.Paciente
        fields = ["nombre","apellido","DNI","obraSocial","numeroAfiliado","historiaClinica","medico_tratante"]