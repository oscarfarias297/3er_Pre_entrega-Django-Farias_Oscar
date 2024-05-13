from django.contrib import admin
from . import models

admin.site.register(models.Medicos)
admin.site.register(models.Especialidad)
admin.site.register(models.Nacionalidad)