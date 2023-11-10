from django.db import models


class proyecto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
   

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.id)