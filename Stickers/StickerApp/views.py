from django.shortcuts import render
from .forms import CarritoForm
from .models import Sticker

# Create your views here.

stickers = Sticker.objects.all()
for sticker in stickers: 
    print (sticker.imagen.url)

def index (request):
    context = {'stickers': stickers, 'titulo': 'Catálogo'}
    return render (request, "index.html", context)

def individual (request, name):
    context = {'stickers': stickers, 'titulo': name}
    return render (request, "individual.html", context)

def novedades (request):
    novedades = ['nov1']
    context = {'novedades': novedades, 'titulo':'Novedades'}
    return render (request, "novedades.html", context)

def carrito (request):
    carrito = CarritoForm()
    context = {'stickers': stickers, 'titulo':'Carrito de compras', 'carrito': carrito}
    return render (request, "carrito.html", context)