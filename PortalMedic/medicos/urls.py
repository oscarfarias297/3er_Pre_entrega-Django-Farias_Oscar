from django.urls import path

from medicos.views import index, medicos_list, confirmar_eliminar, medicos_modificar, medicos_create

app_name = "medicos"

urlpatterns = [
    path("", index, name="index"),
    path("medicos/list", medicos_list ,name="medicos_list"),
    path("medicos/medicos_confirmar_eliminar/<int:pk>", confirmar_eliminar ,name="medicos_confirmar_eliminar"),
    path("medicos/medicos_form/<int:pk>", medicos_modificar, name="medicos_modificar"),
    path("medicos/medicos_create/", medicos_create, name="medicos_create"),

]