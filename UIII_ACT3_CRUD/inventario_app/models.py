from django.db import models

# Create your models here.

class Inventario(models.Model):
    id_inventario = models.CharField(primary_key=True, max_length=6)
    vehiculo = models.CharField(max_length=100)
    cantidad_auto = models.BigIntegerField()
    ubicacion = models.CharField(max_length=100)
    estado_bmr = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)

    def __str__(self):
        return self.vehiculo