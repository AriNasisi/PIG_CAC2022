from django.db import models

# Create your models here.

class Sticker(models.Model):
    nombre: models.CharField(max_length=20, verbose_name='Nombre')
    imagen: models.ImageField(upload_to='stickers')
    fecha: models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.nombre

class Comprador(models.Model):
    nombre: models.CharField(max_length=20, verbose_name='Nombre')
    apellido: models.CharField(max_length=20, verbose_name='Apellido')
    mail: models.EmailField(max_length=100)
    contraseña: models.CharField(max_length=20, verbose_name='Password')

class Pedido(models.Model):

    # Agregamos tupla con opciones
    ESTADO_PEDIDO = ('En revisión', 'Aceptado', 'Rechazado', 'En preparación', 'Listo para retirar', 'Retirado')
    ESTADO_PAGO = ('Aceptado', 'Rechazado')

    # Argumentos del modelo
    comprador: models.ForeignKey(Comprador, on_delete=models.CASCADE)
    fecha: models.DateTimeField(auto_now_add=True)
    estado: models.CharField(max_length=1, choices=ESTADO_PEDIDO)
    estado_de_pago: models.CharField(max_length=1, choices=ESTADO_PAGO)


class Item_pedido(models.Model):

    # Agregamos tupla con opciones
    TAMAÑO_STICKER = (('G','Grande'), ('M','Mediano'), ('C','Chico'))

    # Argumentos del modelo
    pedido: models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sticker: models.ForeignKey(Sticker, on_delete=models.CASCADE)
    cantidad: models.IntegerField(max_length=3)
    tamaño: models.CharField(max_length=1, choices=TAMAÑO_STICKER)
    


