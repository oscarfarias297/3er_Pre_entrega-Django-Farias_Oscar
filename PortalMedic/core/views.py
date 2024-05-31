from django.shortcuts import render,redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

def index(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    next_page = "core/index.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index') 
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

def video_presentacion(request):
    return render(request, "core/video_presentacion.html")