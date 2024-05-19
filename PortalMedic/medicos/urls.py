from django.urls import path

from medicos.views import (index, 
                            medicos_list, 
                            medicos_create, 
                            medicos_update, 
                            medicos_delete,
                            confirmar_eliminar)

app_name = "medicos"

urlpatterns = [
    path("", index, name="index"),
    path("medicos/list", medicos_list ,name="medicos_list"),
    path("medicos/medicos_create/", medicos_create, name="medicos_create"),
    path("medicos/medicos_update/<int:pk>/", medicos_update, name="medicos_update"),
    path("medicos/medicos_delete/<int:pk>/", medicos_delete, name="medicos_delete"),
    path("medicos/medicos_confirm_delete/<int:pk>/", confirmar_eliminar ,name="medicos_confirm_delete"),
]