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
    pedido = {Pedido.comprador: User}
    carrito = CarritoForm()
    context = {'stickers': stickers, 'titulo':'Carrito de compras', 'carrito': carrito}
    return render (request, "carrito.html", context)

def agregarCarrito (request):
    if request.method == 'POST':
        pedidoPendiente = Pedido.objects.filter(estado = 'En revisión').filter(comprador = request.user)
        if pedidoPendiente:
            itemPedido =  Item_pedido(pedido=pedidoPendiente, sticker=request.sticker.id)
            return redirect ("index")
        else:
            nuevoPedido = Pedido(comprador = request.user)
            itemPedido =  Item_pedido(pedido=nuevoPedido, sticker=request.sticker.id)
            return redirect ("index")
        
