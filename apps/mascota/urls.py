from django.conf.urls import url
from .views import index, mascota_view, mascota_list, vacuna_add, vacuna_list, raza_add, raza_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^vacuna/nuevo', vacuna_add, name='vacuna_crear'),
    url(r'^vacuna/listar', vacuna_list, name='vacuna_listar'),
    url(r'^raza/nuevo', raza_add, name='raza_crear'),
    url(r'^raza/listar', raza_list, name='raza_listar'),
]
