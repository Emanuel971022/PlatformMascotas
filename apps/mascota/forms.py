from django import forms
from apps.mascota.models import Mascota, Vacuna, Raza

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'raza',
            'persona',
            'vacuna',
        ]

        label = {
            'nombre':'Nombre',
            'sexo':'Sexo',
            'edad_aproximada':'Edad aproximada',
            'fecha_rescate':'Fecha de rescate',
            'raza':'Raza',
            'persona':'Adoptante',
            'vacuna':'Vacunas',
        }

        CHOICES = [('Macho', 'Macho'), ('Hembra', 'Hembra')]

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.RadioSelect(choices=CHOICES),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class':'form-control'}),
            'raza': forms.Select(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
}

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna

        fields = [
            'nombre',
            'descripcion',
        ]

        label = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción del medicamento',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza

        fields = [
            'nombre',
            'descripcion',
        ]

        label = {
            'nombre': 'Nombre',
            'descripcion': 'Información de la raza',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }