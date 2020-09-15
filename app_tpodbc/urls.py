from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('buscar_cliente', views.buscar_cliente, name='buscar_cliente'),
    path('seleccionar_cliente', views.seleccionar_cliente, name='seleccionar_cliente'),
    path('modificar_cliente/<int:client_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente', views.eliminar_cliente, name='eliminar_cliente')
]
