from django.shortcuts import render
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"