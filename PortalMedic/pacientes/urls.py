from django.urls import path,include

from pacientes.views import index

app_name = "pacientes"

urlpatterns = [
    path("", index, name="index"),
]