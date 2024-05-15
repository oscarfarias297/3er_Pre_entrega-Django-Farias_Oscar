from django import forms

from . import models

class MedicosForm(forms.ModelForm):
    
    class Meta:
        model = models.Medicos
        fields = ["nombre", "apellido","DNI","nacionalidad","matricula","especialidad"]