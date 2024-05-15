from django.db import models
from medicos.models import Medicos

class ObraSocial(models.Model):
    obra_social = models.CharField(max_length=100,unique=True,null=False,blank=False)


class Paciente(models.Model):
    nombre = models.CharField(max_length=50, null = False)
    apellido = models.CharField(max_length=50, null = False)
    DNI = models.IntegerField(unique=True, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    Obra_Social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, blank=True)
    HC = models.TextField(null=False, blank=False)
    #medico_tratante = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True, blank=True)
