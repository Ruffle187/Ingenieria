from django.db import models

# Create your models here.
class Persona(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Telefono = models.IntegerField(max_length=100)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Producto(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)


    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Compra(models.Model):
    Persona = models.ForeignKey(Persona)
    Producto = models.ForeignKey(Producto)
    Fecha = models.DateField( (u"Fecha de compra"), auto_now_add=True, blank=True)
    Hora = models.TimeField( (u"Hora de compra"), auto_now_add=True, blank=True)

    def __str__(self):
        return '%s compra %s' % (self.Persona, self.Producto)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
