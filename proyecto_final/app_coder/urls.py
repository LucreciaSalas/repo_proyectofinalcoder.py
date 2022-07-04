from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", views.inicio, name="inicio"),
    path("about_me", views.about_me, name="about_me"),
    path("pacientes", views.pacientes, name="pacientes"),
    path("prestadores", views.prestadores, name="prestadores"),
    path("proveedores", views.proveedores, name="proveedores"),
    #path("lista_pacientes", views.lista_pacientes),
    #path("lista_prestadores", views.lista_prestadores),
    #path("lista_proveedores", views.lista_proveedores),
    #path("alta_pacientes", views.alta_pacientes),
    path("alta_pacientes", views.formulario_pacientes),
    path("alta_prestadores", views.formulario_prestadores),
    path("alta_proveedores", views.formulario_proveedores),
    path("buscar_prestador", views.buscar_prestador),
    path("buscar_paciente", views.buscar_paciente),
    path("buscar_proveedor", views.buscar_proveedor),
    path("buscarpre", views.busquedaprestador),
    path("buscarpac", views.busquedapaciente),
    path("buscarpro", views.busquedaproveedor),
    path("elimina_paciente/<int:id>", views.elimina_paciente, name="elimina_paciente"), # agregada CLASE 22 chequear funcionamiento 
    path("elimina_prestador/<int:id>", views.elimina_prestador, name="elimina_prestador"), # agregada CLASE 22 chequear funcionamiento 
    path("elimina_proveedor/<int:id>", views.elimina_proveedor, name="elimina_proveedor"), # agregada CLASE 22 chequear funcionamiento
    path("editar_paciente/<int:id>", views.editar_paciente, name="editar_paciente"),
    path("editar_paciente/", views.editar_paciente, name="editar_paciente"),    
    path("editar_prestador/<int:id>", views.editar_prestador, name="editar_prestador"),
    path("editar_prestador/", views.editar_prestador, name="editar_prestador"),
    path("editar_proveedor/<int:id>", views.editar_proveedor, name="editar_proveedor"),
    path("editar_proveedor/", views.editar_proveedor, name="editar_proveedor"),
    path("agenda", views.agenda, name="agenda"),
    path("mensajes_internos", views.mensajes_internos, name="mensajes_internos"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"), #no necesita creación view#
    path("editarPerfil", views.editarPerfil, name= 'editarPerfil')

]