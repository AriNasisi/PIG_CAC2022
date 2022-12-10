from django import forms
from django.core import validators
from django.forms import ValidationError
from StickerApp.models import Item_pedido

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Item_pedido
        fields = ['cantidad', 'tamaño']