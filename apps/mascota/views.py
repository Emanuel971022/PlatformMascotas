from django.shortcuts import render, redirect
from .forms import MascotaForm, VacunaForm, RazaForm
from .models import Mascota, Vacuna, Raza

def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:index')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
    mascota = Mascota.objects.all()
    return render(request, 'mascota/mascota_list.html', {'mascotas':mascota})

def vacuna_add(request):
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:index')
    else:
        form = VacunaForm()

    return render(request, 'mascota/vacuna_form.html', {'form': form})

def vacuna_list(request):
    vacuna = Vacuna.objects.all()
    return render(request, 'mascota/vacuna_list.html', {'vacunas':vacuna})

def raza_add(request):
    if request.method == 'POST':
        form = RazaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:index')
    else:
        form = RazaForm()

    return render(request, 'mascota/raza_form.html', {'form': form})

def raza_list(request):
    raza = Raza.objects.all()
    return render(request, 'mascota/raza_list.html', {'razas':raza})