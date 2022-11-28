from django.db import models

# Create your models here.

class Sticker(models.Model):
    nombre: models.CharField(max_length=20, verbose_name='Nombre')
    imagen:
        
    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    nombre: