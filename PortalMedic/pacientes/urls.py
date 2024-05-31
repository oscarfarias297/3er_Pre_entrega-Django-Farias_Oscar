from django.urls import path

from pacientes.views import (index,
                            pacientes_list,
                            pacientes_create,
                            pacientes_update,
                            pacientes_delete,
                            confirmar_eliminar,
                            guardar_historia,
                            ver_historia,
                            modificar_hc,
)

app_name = "pacientes"

urlpatterns = [
    path("", index, name="index"),
    path("pacientes/list", pacientes_list,name="pacientes_list" ),
    path("pacientes/pacientes_create/", pacientes_create, name="pacientes_create"),
    path("pacientes/pacientes_update/<int:pk>/", pacientes_update, name="pacientes_update"),
    path("pacientes/pacientes_delete/<int:pk>/", pacientes_delete, name="pacientes_delete"),
    path("pacientes/pacientes_confirm_delete/<int:pk>/", confirmar_eliminar ,name="pacientes_confirm_delete"),
    path("pacientes/<int:pk>/guardar/", guardar_historia, name='guardar_historia'),
    path("pacientes/<int:pk>/ver/", ver_historia, name='ver_historia'),
    path("pacientes/<int:pk>/modificar_hc/", modificar_hc, name='modificar_hc'),
]