from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render (request, "index.html")

def individual (request, id):
    return HttpResponse(f'item {id}')