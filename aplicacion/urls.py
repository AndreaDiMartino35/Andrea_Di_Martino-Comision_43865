from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),

    path('clientes/', ClienteList.as_view(), name="clientes"),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente"),
    path('detail_cliente/<int:pk>/', ClienteDetail.as_view(), name="detail_cliente"),
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),

    path('criaderos/', CriaderoList.as_view(), name="criaderos"),
    path('create_criaderos/', CriaderoCreate.as_view(), name="create_criaderos"),
    path('detail_criadero/<int:pk>/', CriaderoDetail.as_view(), name="detail_criadero"),
    path('update_criadero/<int:pk>/', CriaderoUpdate.as_view(), name="update_criadero"),
    path('delete_criadero/<int:pk>/', CriaderoDelete.as_view(), name="delete_criadero"),

    path('tambos/', TamboList.as_view(), name="tambos"),
    path('create_tambo/', TamboCreate.as_view(), name="create_tambo"),
    path('detail_tambo/<int:pk>/', TamboDetail.as_view(), name="detail_tambo"),
    path('update_tambo/<int:pk>/', TamboUpdate.as_view(), name="update_tambo"),
    path('delete_tambo/<int:pk>/', TamboDelete.as_view(), name="delete_tambo"),

    path('agricultores/', AgricultorList.as_view(), name="agricultores"),
    path('create_agricultor/', AgricultorCreate.as_view(), name="create_agricultor"),
    path('detail_agricultor/<int:pk>/', AgricultorDetail.as_view(), name="detail_agricultor"),
    path('update_agricultor/<int:pk>/', AgricultorUpdate.as_view(), name="update_agricultor"),
    path('delete_agricultor/<int:pk>/', AgricultorDelete.as_view(), name="delete_agricultor"),

    path('buscar/', buscar, name="buscar"),
    path('buscar_email/', buscarEmail, name="buscar_email"),
    path('acerca/', acerca, name="acerca"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_usuario/', editarUsuario, name="editar_usuario"),
    path('agregar_foto/', agregarFoto, name="agregar_foto"),
]