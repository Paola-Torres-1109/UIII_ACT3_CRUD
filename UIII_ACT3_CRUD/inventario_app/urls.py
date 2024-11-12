from django.urls import path
from inventario_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarInventario/", views.registrarInventario, name="registrarInventario"),
    path("seleccionarInventario/<id_inventario>", views.seleccionarInventario, name="seleccionarInventario"),
    path("editarInventario/<id_inventario>", views.editarInventario, name="editarInventario"),
    path("borrarInventario/<id_inventario>", views.borrarInventario, name="borrarInventario")
    ]
