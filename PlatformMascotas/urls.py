from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^mascota/', include('apps.mascota.urls', namespace="mascota")),
    url(r'^adopcion/', include('apps.adopcion.urls', namespace="adopcion")),
    url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout')
]
