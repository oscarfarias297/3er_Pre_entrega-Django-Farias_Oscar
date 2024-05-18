from django.db import models


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.especialidad
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.nacionalidad
    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidad"



class Medicos(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    apellido = models.CharField(max_length=100, null=False, blank=True)
    DNI = models.PositiveIntegerField(unique=True,null=True)
    nacionalidad= models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True)
    matricula = models.PositiveIntegerField(unique=True, null=False, blank=False,verbose_name="Matricula Nacional")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Medicos"
        verbose_name_plural = "Medicos"


# class Paciente(models.Model):
#     nombre = models.CharField(max_length=50, null = False)
#     apellido = models.CharField(max_length=50, null = False)
#     DNI = models.IntegerField(unique=True, null=False)
#     telefono = models.IntegerField(null=True)
#     nacionalidad= models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True)
#     medico_tratante = models.ForeignKey(Medicos, on_delete=models.SET_NULL, null=True)

#     def __str__(self) -> str:
#         return f"{self.apellido}, {self.nombre}"

#     class Meta:
#         verbose_name = "Paciente"
#         verbose_name_plural = "Pacientes"