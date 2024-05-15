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
    Obra_Social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, blank=True)
    numero_afiliado = models.CharField(max_length=50)
    HC = models.TextField()
    #medico_tratante = models.ForeignKey("medicos.Medicos", on_delete=models.SET_NULL, null=True, blank=True)
