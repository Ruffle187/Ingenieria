from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Compra(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.DateField(_(u"Fecha de compra"), auto_now_add=True, blank=True)
    hora = models.TimeField(_(u"Hora de compra"), auto_now_add=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
