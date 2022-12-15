from django.contrib import admin

# Register your models here.
from .models import Pedido, Item_pedido, Sticker, Personalizados

class Item_pedidoInline(admin.TabularInline):
    model = Item_pedido

class PedidoAdmin(admin.ModelAdmin):
    fields = ('comprador', 'estado', 'estado_de_pago')
    
    #list of fields to display in django admin
    list_display = ['id', 'comprador', 'fecha', 'estado', 'estado_de_pago']
    
    inlines = [
        Item_pedidoInline,
    ]

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Item_pedido)
admin.site.register(Sticker)
admin.site.register(Personalizados)
