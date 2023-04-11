
from django.urls import path, include
from inicio.views import mi_vista, mi_primer_template, mostrar_fecha, crear_animal, prueba_template



urlpatterns = [
    path('', mi_vista),
    path('mi-primer-template/', mi_primer_template),
    path('mostrar-fecha/', mostrar_fecha),
    path('crear-animal/', crear_animal),
    path('prueba-template/', prueba_template)
]


from django.urls import path

from inicio import views





# urlpatterns = [
   
#     path('', views.inicio, name="Inicio"), #esta era nuestra primer view
#     path('cursos', views.cursos, name="Cursos"),
#     path('auto', views.auto, name="Auto"),
#     path('estudiantes', views.estudiantes, name="Estudiantes"),
#     path('entregables', views.entregables, name="Entregables"),
    
    
#     path('Sensores', views.Sensores, name="Sensores"),
#     path('Usuario', views.Usuario, name="Usuario"),
#     path('DatosPersonales', views.DatosPersonales, name="DatosPersonales"),
    
    
#     #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
#     #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
#     #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
#     path('buscar/', views.buscar),
#     path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
#     path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
#     path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
#     path('curso/list', views.CursoList.as_view(), name='List'),
#     path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
#     path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
#     path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
#     path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
#     path(r'^editar/(?P<pk>\d+)$', views.DatosPersonalesUpdate.as_view(), name='Edit'),
#     path(r'^refrescar/(?P<pk>\d+)$', views.DatosPersonalesDetalle.as_view(), name='Refrescar'),
    

# ]

