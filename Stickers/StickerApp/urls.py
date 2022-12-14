from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('novedades/', views.novedades, name='novedades'),
    path('item/<int:pk>/', views.individual, name='individual'),
    path('carrito/', views.carrito, name='carrito'),
    # path('agregar_carrito/<int:pk>/', views.agregarCarrito, name='agregarCarrito'),
    path("crear_usuario", views.crearUsuario, name="crear_usuario"),
    path('eliminar/<int:pk>/', views.eliminarDelCarrito, name='eliminarDelCarrito'),
    path('finalizado/', views.finalizarPedido, name='finalizado'),
    path('personalizados/', views.personalizados, name='personalizados')


]