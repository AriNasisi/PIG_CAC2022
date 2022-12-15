from django.shortcuts import render, redirect
from .forms import CarritoForm, PersonalizadosForm
from .models import Sticker, Pedido, Item_pedido, Personalizados
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    stickers = Sticker.objects.all()
    context = {'stickers': stickers, 'titulo': 'Catálogo'}
    return render(request, "index.html", context)


def individual(request, pk):
    sticker = Sticker.objects.get(id=pk)
    url2 = '/StickerApp/#'+str(sticker.id)
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if form.is_valid():
            tamaño = form.cleaned_data.get('tamaño')
            cantidad = form.cleaned_data.get('cantidad')
            try:
                pedidoPendiente = Pedido.objects.get(estado='1', comprador=request.user)
                itemPedido = Item_pedido(pedido=pedidoPendiente, sticker=sticker, cantidad=cantidad, tamaño=tamaño)
                itemPedido.save()

                return redirect(url2)

            except Pedido.DoesNotExist:
                nuevoPedido = Pedido(comprador=request.user)
                nuevoPedido.save()
                itemPedido = Item_pedido(pedido=nuevoPedido, sticker=sticker, tamaño=tamaño, cantidad=cantidad)
                itemPedido.save()
                return redirect(url2)


    sticker = Sticker.objects.get(id=pk)
    carritoForm = CarritoForm()
    context = {'sticker': sticker, 'titulo': sticker, 'carritoForm': carritoForm}
    return render(request, "individual.html", context)
 
def personalizados(request):
    if request.method == 'POST':
        form = PersonalizadosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            link = form.cleaned_data.get('link_imagen')
            email = form.cleaned_data.get('email')
            nuevoPersonalizado = Personalizados(nombre=nombre, link_imagen=link, email=email)
            nuevoPersonalizado.save()
            return render(request, "rta_personalizados.html")
    
    personalizado = PersonalizadosForm()
    context = {'personalizado': personalizado}
    return render(request, "personalizados.html", context)


def novedades(request):
    stickers = Sticker.objects.filter(esNovedad=True)
    context = {'stickers': stickers, 'titulo': 'Novedades'}
    return render(request, "novedades.html", context)


@login_required
def carrito(request):
    try:        
        pedidoPendiente = Pedido.objects.get(estado='1', comprador=request.user)
        stickersCarrito = pedidoPendiente.item_pedido_set.all()
        context = {'stickersCarrito': stickersCarrito, 'titulo': 'Carrito de compras', 'carrito': carrito}
        return render(request, "carrito.html", context)
    except Pedido.DoesNotExist:
        return render(request=request, template_name='carrito_vacio.html')

def crearUsuario(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario creado con éxito")
            return redirect("index")
        messages.error(
            request, "Error. Información invalida!")
    form = NewUserForm()
    return render(request=request, template_name="registration.html", context={"register_form": form})

@login_required
def eliminarDelCarrito(request, pk):
    stickerEliminar = Item_pedido.objects.get(id=pk)
    stickerEliminar.delete()
    return redirect('/StickerApp/carrito/#inicio')


@login_required
def finalizarPedido(request):
    Pedido.objects.filter(estado='1', comprador=request.user).update(estado='2')
    
    return render(request=request, template_name='finalizado.html')


