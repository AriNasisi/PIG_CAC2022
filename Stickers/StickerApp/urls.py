from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('novedades/', views.novedades, name='novedades'),
    path('item/<str:name>', views.individual, name='individual'),
    path('carrito/', views.carrito, name='carrito'),
    

] 