from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


class Nacionalidad(models.Models):
    pais = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.pais


class Medico(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    apellido = models.CharField(max_length=100, null=False, blank=True)
    DNI = models.PositiveIntegerField(unique=True,null=True)
    nacionalidad= models.CharField(Nacionalidad, on_delete=models.SET_NULL, null=False,blank=False)
    matricula = models.PositiveIntegerField(unique=True, null=False, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL,null=False, blank=True)
