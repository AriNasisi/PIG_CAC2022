from django import forms
from django.core import validators
from django.forms import ValidationError
from StickerApp.models import Item_pedido
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CarritoForm(forms.ModelForm):
    class Meta:
        model = Item_pedido
        fields = ['cantidad', 'tamaño']


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class PersonalizadosForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    link_imagen = forms.URLField(label='Link imagen', required=True)
    email = forms.EmailField(required=True)
