from django.db import models


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.pais
    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidad"



class Medico(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    apellido = models.CharField(max_length=100, null=False, blank=True)
    DNI = models.PositiveIntegerField(unique=True,null=True)
    nacionalidad= models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True)
    matricula = models.PositiveIntegerField(unique=True, null=False, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)