from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "aplicacion/base.html")

def buscar(request):
    if request.GET['email']:
        email = request.GET['email']
        clientes = Cliente.objects.filter(email__icontains=email)
        return render(request, "aplicacion/resultadosEmail.html", {"email": email, "clientes": clientes})
    return HttpResponse("No se ingresaron datos para buscar")

def buscarEmail(request):
    return render(request, "aplicacion/buscarEmail.html")

def acerca(request):
    return render(request, "aplicacion/acerca.html")

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

class CriaderoList(LoginRequiredMixin, ListView):
    model = Criadero

class CriaderoCreate(LoginRequiredMixin, CreateView):
    model = Criadero
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('criaderos')

class CriaderoDetail(LoginRequiredMixin, DetailView):
    model = Criadero

class CriaderoUpdate(LoginRequiredMixin, UpdateView):
    model = Criadero
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('criaderos')

class CriaderoDelete(LoginRequiredMixin, DeleteView):
    model = Criadero
    success_url = reverse_lazy('criaderos')

class TamboList(LoginRequiredMixin, ListView):
    model = Tambo

class TamboCreate(LoginRequiredMixin, CreateView):
    model = Tambo
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('tambos')

class TamboDetail(LoginRequiredMixin, DetailView):
    model = Tambo

class TamboUpdate(LoginRequiredMixin, UpdateView):
    model = Tambo
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('tambos')

class TamboDelete(LoginRequiredMixin, DeleteView):
    model = Tambo
    success_url = reverse_lazy('tambos')

class AgricultorList(LoginRequiredMixin, ListView):
    model = Agricultor

class AgricultorCreate(LoginRequiredMixin, CreateView):
    model = Agricultor
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('agricultores')

class AgricultorDetail(LoginRequiredMixin, DetailView):
    model = Agricultor

class AgricultorUpdate(LoginRequiredMixin, UpdateView):
    model = Agricultor
    fields = ['nombre', 'cuit', 'email']
    success_url = reverse_lazy('agricultores')

class AgricultorDelete(LoginRequiredMixin, DeleteView):
    model = Agricultor
    success_url = reverse_lazy('agricultores')

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    foto = Foto.objects.get(user=request.user.id).imagen.url
                except:
                    foto = '/media/imagenes/default.png'
                finally:
                    request.session['foto'] = foto

                return render(request, "aplicacion/base.html", {"mensaje": f"Hola {usuario}!"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Usuario no registrado - Intente nuevamente"})
        else:
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Usuario no registrado - Intente nuevamente"})
            return render(request, "aplicacion/base.html")

    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form":miForm})   

def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario creado exitosamente"})
    else:
        form = RegistroUsuariosForm()
    return render(request, "aplicacion/registro.html", {"form": form})      

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')  
            usuario.password1 = form.cleaned_data.get('password1') 
            usuario.password2 = form.cleaned_data.get('password2') 
            usuario.first_name = form.cleaned_data.get('first_name') 
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} se ha actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarUsuario.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "aplicacion/editarUsuario.html", {'form': form, 'usuario': usuario.username})
    
@login_required
def agregarFoto(request):
    if request.method == "POST":
        form = FotoFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            fotoVieja = Foto.objects.filter(user=u)
            if len(fotoVieja) > 0:
                fotoVieja[0].delete

            foto = Foto(user=u, imagen=form.cleaned_data['imagen'])
            foto.save()

            imagen = Foto.objects.get(user=request.user.id).imagen.url
            request.session['foto'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = FotoFormulario()
        return render(request, "aplicacion/agregarFoto.html", {'form': form})
    
