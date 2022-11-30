from django.shortcuts import render
from StickerApp.forms import CarritoForm

# Create your views here.

stickers = ['Primer Stk', 'Segundo Stk', 'Tercer Stk', 'Cuarto Stk', 'Quinto Stk', 'Sexto Stk']

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