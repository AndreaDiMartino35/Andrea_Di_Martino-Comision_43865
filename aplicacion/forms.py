from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cliente", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del cliente", max_length=50, required=True)
    email = forms.EmailField(label="Email del cliente", required=True)

class CriaderoForm(forms.Form):
     nombre = forms.CharField(label="Nombre del criadero", max_length=50, required=True)
     cuit = forms.IntegerField(label="CUIT", required=True)
     email = forms.EmailField(label="Email del criadero", required=True)

class TamboForm(forms.Form):
     nombre = forms.CharField(label="Nombre del tambo", max_length=50, required=True)
     cuit = forms.IntegerField(label="CUIT", required=True)
     email = forms.EmailField(label="Email del tambo", required=True)

class AgricultorForm(forms.Form):
     nombre = forms.CharField(label="Nombre del agricultor", max_length=50, required=True)
     cuit = forms.IntegerField(label="CUIT", required=True)
     email = forms.EmailField(label="Email del agricultor", required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario") 
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario") 
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class FotoFormulario(forms.Form):
    imagen = forms.ImageField(required=True)