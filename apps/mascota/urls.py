from django.conf.urls import url
from .views import index,\
    mascota_view, mascota_list, mascota_detail, mascota_edit, mascota_delete, \
    vacuna_add, vacuna_list, vacuna_detail, vacuna_edit, vacuna_delete, \
    raza_add, raza_list, raza_detail, raza_edit, raza_delete

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^detalles/(?P<id_mascota>\d+)/$', mascota_detail, name='mascota_detalles'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),

    url(r'^vacuna/nuevo', vacuna_add, name='vacuna_crear'),
    url(r'^vacuna/listar', vacuna_list, name='vacuna_listar'),
    url(r'^vacuna/detalles/(?P<id_vacuna>\d+)/$', vacuna_detail, name='vacuna_detalles'),
    url(r'^vacuna/editar/(?P<id_vacuna>\d+)/$', vacuna_edit, name='vacuna_editar'),
    url(r'^vacuna/eliminar/(?P<id_vacuna>\d+)/$', vacuna_delete, name='vacuna_eliminar'),

    url(r'^raza/nuevo', raza_add, name='raza_crear'),
    url(r'^raza/listar', raza_list, name='raza_listar'),
    url(r'^raza/detalles/(?P<id_raza>\d+)/$', raza_detail, name='raza_detalles'),
    url(r'^raza/editar/(?P<id_raza>\d+)/$', raza_edit, name='raza_editar'),
    url(r'^raza/eliminar/(?P<id_raza>\d+)/$', raza_delete, name='raza_eliminar'),

]
