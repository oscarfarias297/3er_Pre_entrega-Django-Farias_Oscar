from django.urls import path,include

from pacientes.views import index,pacientes_list

app_name = "pacientes"

urlpatterns = [
    path("", index, name="index"),
    path("pacientes/list",pacientes_list,name="pacientes_list"),
]