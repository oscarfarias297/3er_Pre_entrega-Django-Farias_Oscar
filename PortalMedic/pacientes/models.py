from django.db import models

class ObraSocial(models.Model):
    obra_social = models.CharField(max_length=100,unique=True,null=False,blank=False)
    def __str__(self) -> str:
        return self.obra_social
    
    class Meta:
        verbose_name = "Obra Social"
        verbose_name_plural = "Obras Sociales"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, null = False)
    apellido = models.CharField(max_length=50, null = False)
    DNI = models.IntegerField(unique=True, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    obraSocial = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, blank=True, verbose_name = "Socio ID", related_name="paciente_obrasocial")
    numeroAfiliado = models.CharField(max_length=50,null=False, blank=False, verbose_name="Numero de Afiliado")
    historiaClinica = models.TextField(null=True, blank=True)
    medico_tratante = models.ForeignKey("medicos.Medicos", on_delete=models.SET_NULL, null=True, blank=True, related_name="paciente_medicos")

    def __str__(self) -> str:
        return (f"{self.apellido}, {self.nombre}")
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"