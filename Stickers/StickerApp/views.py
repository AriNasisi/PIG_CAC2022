from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

stickers = ['Primer Stk', 'Segundo Stk', 'Tercer Stk', 'Cuarto Stk', 'Quinto Stk', 'Sexto Stk']

def index (request):
    
    context = {'stickers': stickers, 'titulo': 'Catálogo'}
    return render (request, "index.html", context)

def individual (request, name):
    id = stickers.index(name)
    individual = stickers[id]
    context = {'stickers': stickers, 'titulo': id+1, 'individual': individual}
    return render (request, "individual.html", context)