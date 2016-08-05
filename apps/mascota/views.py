from django.shortcuts import render, redirect
from .forms import MascotaForm, VacunaForm, RazaForm
from .models import Mascota, Vacuna, Raza
from apps.adopcion.models import Persona

def index(request):
    return render(request, 'mascota/index.html')

"""
    Vistas relacionadas con las mascotas
"""

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
    return render(request, 'mascota/mascota_list.html', {'mascotas':mascota, 'is_Specific':'General'})

def mascota_detail(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    vacunas = mascota.vacuna.all()
    return render(request, 'mascota/mascota_detail.html', {'mascota': mascota, 'vacunas':vacunas})

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == "GET":
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')

    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})

def mascota_mascotasPersona(request, persona_id):
    mascotasDueno = Mascota.objects.all().filter(persona_id = persona_id)
    persona = Persona.objects.get(id=persona_id)
    return render(request, 'mascota/mascota_list.html', {'mascotas':mascotasDueno, 'persona':persona, 'is_Specific':'Adoptante'},)

"""
    Vistas relacionadas con las vacunas
"""

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

def vacuna_detail(request, id_vacuna):
    vacuna = Vacuna.objects.get(id=id_vacuna)
    return render(request, 'mascota/vacuna_detail.html', {'vacuna':vacuna})

def vacuna_edit(request, id_vacuna):
    vacuna = Vacuna.objects.get(id=id_vacuna)
    if request.method == 'GET':
        form = VacunaForm(instance=vacuna)
    else:
        form = VacunaForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
        return redirect('mascota:vacuna_listar')

    return render(request, 'mascota/vacuna_form.html', {'form':form})

def vacuna_delete(request, id_vacuna):
    vacuna = Vacuna.objects.get(id=id_vacuna)
    if request.method == 'POST':
        vacuna.delete()
        return redirect('mascota:vacuna_listar')
    return render(request, 'mascota/vacuna_delete.html', {'vacuna': vacuna})

def vacuna_MascotasVacuna(request, id_vacuna):
    vacunas = Vacuna.objects.get(id=id_vacuna)
    MascotasVacuna = vacunas.mascota_set.all()
    return render(request, 'mascota/mascota_list.html', {'mascotas':MascotasVacuna, 'Vacuna':vacunas, 'is_Specific':'Vacunas'},)

"""
    Vistas relacionadas con las razas
"""

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

def raza_detail(request, id_raza):
    raza = Raza.objects.get(id=id_raza)
    return render(request, 'mascota/raza_detail.html', {'raza':raza})

def raza_edit(request, id_raza):
    raza = Raza.objects.get(id=id_raza)
    if request.method == 'GET':
        form = RazaForm(instance=raza)
    else:
        form = RazaForm(request.POST, instance=raza)
        if form.is_valid():
            form.save()
        return redirect('mascota:raza_listar')

    return render(request, 'mascota/raza_form.html', {'form':form})

def raza_delete(request, id_raza):
    raza = Raza.objects.get(id=id_raza)
    if request.method == 'POST':
        raza.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/raza_delete.html', {'raza': raza})