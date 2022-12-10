from django.contrib import admin

# Register your models here.
from .models import Pedido, Item_pedido, Sticker


admin.site.register(Pedido)
admin.site.register(Item_pedido)
admin.site.register(Sticker)
