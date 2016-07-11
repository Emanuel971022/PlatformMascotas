from django.contrib import admin
from apps.mascota.models import Mascota, Vacuna, Raza

admin.site.register(Mascota)
admin.site.register(Vacuna)
admin.site.register(Raza)