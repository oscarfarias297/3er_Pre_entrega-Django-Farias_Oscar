from django.urls import path

from core.views import index, CustomLoginView

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
]