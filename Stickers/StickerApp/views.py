from django.shortcuts import render, redirect
from .forms import CarritoForm
from .models import Sticker, Pedido, Item_pedido
from django.contrib.auth.models import User

# Create your views here.


def index (request):
    stickers = Sticker.objects.all()
    context = {'stickers': stickers, 'titulo': 'Catálogo'}
    return render (request, "index.html", context)

def individual (request, name):
    stickers = Sticker.objects.all()
    context = {'stickers': stickers, 'titulo': name}
    return render (request, "individual.html", context)

def novedades (request):
    stickers = Sticker.objects.filter(esNovedad = True)
    context = {'stickers': stickers, 'titulo':'Novedades'}
    return render (request, "novedades.html", context)

def carrito (request):
    pedidoPendiente = Pedido.objects.get(estado = 'En revisión', comprador = request.user)
    stickersCarrito = pedidoPendiente.item_pedido_set.all()
    carrito = CarritoForm()
    context = {'stickersCarrito': stickersCarrito, 'titulo':'Carrito de compras', 'carrito': carrito}
    return render (request, "carrito.html", context)

def agregarCarrito (request, pk):

    sticker = Sticker.objects.get(id=pk)
    try:
        pedidoPendiente = Pedido.objects.get(estado = 'En revisión', comprador = request.user)

    except Pedido.DoesNotExist:
        nuevoPedido = Pedido(comprador = request.user)
        nuevoPedido.save()
        itemPedido =  Item_pedido(pedido=nuevoPedido, sticker=sticker)
        itemPedido.save()
        return redirect ("index")
    print(pedidoPendiente.id)
    itemsDelPedido = pedidoPendiente.item_pedido_set.all()
    print(itemsDelPedido)
    itemPedido =  Item_pedido(pedido=pedidoPendiente, sticker=sticker)
    itemPedido.save()
    return redirect ("index")

        
        
