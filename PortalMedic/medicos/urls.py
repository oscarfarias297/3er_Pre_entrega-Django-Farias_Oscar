from django.urls import path,include

from medicos.views import index, medicos_list

app_name = "medicos"

urlpatterns = [
    path("", index, name="index"),
    path("medicos/list", medicos_list ,name="medicos_list"),
]