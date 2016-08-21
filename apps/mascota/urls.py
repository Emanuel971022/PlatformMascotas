from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import index,\
    listado, \
    mascota_view, mascota_list, mascota_detail, mascota_edit, mascota_delete, mascota_mascotasPersona, \
    vacuna_add, vacuna_list, vacuna_detail, vacuna_edit, vacuna_delete, vacuna_MascotasVacuna, \
    raza_add, RazaCreate, raza_list, RazaList, raza_detail, raza_edit, RazaUpdate, raza_delete, RazaDelete

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^nuevo$', login_required(mascota_view), name='mascota_crear'),
    url(r'^listar$', login_required(mascota_list), name='mascota_listar'),
    url(r'^detalles/(?P<id_mascota>\d+)/$', login_required(mascota_detail), name='mascota_detalles'),
    url(r'^editar/(?P<id_mascota>\d+)/$', login_required(mascota_edit), name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', login_required(mascota_delete), name='mascota_eliminar'),
    url(r'^adoptante/(?P<persona_id>\d+)/$', login_required(mascota_mascotasPersona), name='mascotas_persona'),

    url(r'^vacuna/nuevo', login_required(vacuna_add), name='vacuna_crear'),
    url(r'^vacuna/listar', login_required(vacuna_list), name='vacuna_listar'),
    url(r'^vacuna/detalles/(?P<id_vacuna>\d+)/$', login_required(vacuna_detail), name='vacuna_detalles'),
    url(r'^vacuna/editar/(?P<id_vacuna>\d+)/$', login_required(vacuna_edit), name='vacuna_editar'),
    url(r'^vacuna/eliminar/(?P<id_vacuna>\d+)/$', login_required(vacuna_delete), name='vacuna_eliminar'),
    url(r'^listar/mascotas/(?P<id_vacuna>\d+)/$', login_required(vacuna_MascotasVacuna), name='vacuna_MascotasAplicadas'),

    url(r'^raza/nuevo', login_required(RazaCreate.as_view()), name='raza_crear'),
    url(r'^raza/listar', login_required(RazaList.as_view()), name='raza_listar'),
    url(r'^raza/detalles/(?P<id_raza>\d+)/$', login_required(raza_detail), name='raza_detalles'),
    url(r'^raza/editar/(?P<pk>\d+)/$', login_required(RazaUpdate.as_view()), name='raza_editar'),
    url(r'^raza/eliminar/(?P<pk>\d+)/$', login_required(RazaDelete.as_view()), name='raza_eliminar'),

    url(r'^listado/', listado, name='listado')
]
