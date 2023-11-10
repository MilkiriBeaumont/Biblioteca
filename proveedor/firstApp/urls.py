from django.urls import path
from . import views

urlpatterns = [
    path('',views.display, name='inicio'),
    path('template',views.template, name='template'),
    path('', views.home),
    path('proyectos/',views.listadoProyecto),
    path('agregarProyecto/',views.agregarProyecto),
]