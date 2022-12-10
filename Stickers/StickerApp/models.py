from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sticker(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='stickers')
    fecha = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.nombre

class Pedido(models.Model):

    # Agregamos tupla con opciones
    ESTADO_PEDIDO = ((1, 'En revisión'), (2,'Aceptado'), (3,'Rechazado'), (4,'En preparación'), (5,'Listo para retirar'), (6,'Retirado'))
    ESTADO_PAGO = ((1,'Aceptado'), (2,'Rechazado'))

    # Argumentos del modelo
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADO_PEDIDO)
    estado_de_pago = models.CharField(max_length=1, choices=ESTADO_PAGO)


class Item_pedido(models.Model):

    # Agregamos tupla con opciones
    TAMAÑO_STICKER = (('G','Grande'), ('M','Mediano'), ('C','Chico'))

    # Argumentos del modelo
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tamaño = models.CharField(max_length=10, choices=TAMAÑO_STICKER)
    


