
from django.urls import path
from inicio.views import mi_vista, mi_primer_template, mostrar_fecha, crear_animal
from fecha_hora.vistas2 import index

urlpatterns = [
    path('', mi_vista),
    path('mi-primer-template/', mi_primer_template),
    path('fecha-hora/', index),
    path('mostrar-fecha/', mostrar_fecha),
    path('crear-animal/', crear_animal)
]
