from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import *
from django.template import loader
from app_coder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request): 
    return render(request, "padre.html")

def about_me(request): 
    return render(request, "aboutme.html")

def agenda(request): 
    return render(request, "agenda_turnos.html")

def mensajes_internos(request): 
    return render(request, "mensajes_internos.html")

def pacientes(request):
    pacientes= Pacientes.objects.all()
    datos= {"pacientes" : pacientes }
    plantilla= loader.get_template("pacientes.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

def prestadores(request):
    prestadores= Prestadores.objects.all()
    datos= {"prestadores" : prestadores }
    plantilla= loader.get_template("prestadores.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

def proveedores(request):
    proveedores= Proveedores.objects.all()
    datos= {"proveedores" : proveedores }
    plantilla= loader.get_template("proveedores.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

@login_required
def formulario_pacientes (request):  #alta pacientes#
    if request.method == "POST":
        mi_formulario= Formulario_pacientes(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            pacientes = Pacientes( nombre=datos['nombre'] , edad=datos['edad'] , dni=datos['dni'] , telefono=datos['telefono'] , email=datos['email'] ) 
            pacientes.save()
            return render (request , "formpacientes.html")

    return render (request , "formpacientes.html")

@login_required
def formulario_proveedores (request): #alta proveedores#
    if request.method == "POST":
        mi_formulario= Formulario_proveedores(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data            
            proveedores = Proveedores( nombre=datos['nombre'] , cuit=datos['cuit'] , cbu=datos['cbu'] , telefono=datos['telefono'] , email=datos['email']) 
            proveedores.save()
            return render (request , "formproveedores.html")
    return render (request , "formproveedores.html")

@login_required
def formulario_prestadores (request): #alta prestadores#
    if request.method == "POST":
        mi_formulario= Formulario_prestadores(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data        
            prestadores = Prestadores( nombre=request.POST['nombre'] , especialidad=request.POST['especialidad'] , telefono=request.POST['telefono'] , email=request.POST['email']) 
            prestadores.save()
        return render (request , "formprestadores.html")
    return render (request , "formprestadores.html")
    
def buscar_prestador(request):
    return render(request, "buscar_prestador.html")

def buscar_paciente(request):
    return render(request, "buscar_paciente.html")

def buscar_proveedor(request):
    return render(request, "buscar_proveedor.html")

def busquedaprestador(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        prestadores= Prestadores.objects.filter(nombre__icontains= nombre)
        return render (request, "resultado_busqueda_prestador.html", {"prestadores": prestadores})
    else:
        return HttpResponse("Campo de búsqueda vacio")     

def busquedapaciente(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        pacientes= Pacientes.objects.filter(nombre__icontains= nombre)
        return render (request, "resultado_busqueda_paciente.html", {"pacientes": pacientes})
    else:
        return HttpResponse("Campo de búsqueda vacio")

def busquedaproveedor(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        proveedores= Proveedores.objects.filter(nombre__icontains= nombre)
        return render (request, "resultado_busqueda_proveedor.html", {"proveedores": proveedores})
    else:
        return HttpResponse("Campo de búsqueda vacio")

@login_required
def elimina_paciente(request, id):
    paciente= Pacientes.objects.get(id=id)
    paciente.delete()

    paciente= Pacientes.objects.all()
    return render(request, "pacientes.html", {"pacientes": paciente}) #ok 

@login_required
def elimina_prestador(request, id):
    prestador= Prestadores.objects.get(id=id)
    prestador.delete()

    prestador= Prestadores.objects.all()
    return render(request, "prestadores.html", {"prestadores": prestador}) #ok

@login_required
def elimina_proveedor(request, id):
    proveedor= Proveedores.objects.get(id=id)
    proveedor.delete()

    proveedor= Proveedores.objects.all()
    return render(request, "proveedores.html", {"proveedores": proveedor}) #ok

@login_required
def editar_paciente (request, id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_pacientes(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            paciente.nombre= datos['nombre']
            paciente.edad= datos['edad'] 
            paciente.dni= datos['dni'] 
            paciente.telefono= datos['telefono'] 
            paciente.email= datos['email']
            paciente.save()
            paciente = Pacientes.objects.all()
            return render (request , "pacientes.html", {"pacientes": paciente})
    else:
        mi_formulario = Formulario_pacientes(initial={'nombre':paciente.nombre, 'edad':paciente.edad, 'dni':paciente.dni, 'telefono':paciente.telefono, 'email':paciente.email})
        
    return render (request , "editar_paciente.html", {"mi_formulario":mi_formulario, "paciente":paciente})

@login_required
def editar_prestador (request, id):
    prestador = Prestadores.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_prestadores(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            prestador.nombre= datos['nombre']
            prestador.especialidad= datos['especialidad'] 
            prestador.telefono= datos['telefono'] 
            prestador.email= datos['email']
            prestador.save()
            prestador = Prestadores.objects.all()
            return render (request , "prestadores.html", {"prestadores": prestador})
    else:
        mi_formulario = Formulario_prestadores(initial={'nombre':prestador.nombre, 'especialidad':prestador.especialidad, 'telefono':prestador.telefono, 'email':prestador.email})
        
    return render (request , "editar_prestador.html", {"mi_formulario":mi_formulario, "prestador":prestador})

@login_required
def editar_proveedor (request, id):
    proveedor = Proveedores.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_proveedores(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            proveedor.nombre= datos['nombre']
            proveedor.cuit= datos['cuit'] 
            proveedor.cbu= datos['cbu'] 
            proveedor.telefono= datos['telefono'] 
            proveedor.email= datos['email']
            proveedor.save()
            proveedor = Proveedores.objects.all()
            return render (request , "proveedores.html", {"proveedores": proveedor})
    else:
        mi_formulario = Formulario_proveedores(initial={'nombre':proveedor.nombre, 'cuit':proveedor.cuit, 'cbu':proveedor.cbu, 'telefono':proveedor.telefono, 'email':proveedor.email})
        
    return render (request , "editar_proveedor.html", {"mi_formulario":mi_formulario, "proveedor":proveedor})


def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                avatares= Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario Incorrecto")

        else:
            return HttpResponse(f"Formulario Incorrecto {form}")  

    form= AuthenticationForm()
    return render (request, "login.html", {"form":form})


def register(request): #permite crear usuarios sin utilizar panel de administrador"
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm
    return render(request, "registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario= request.user
    if request.method == "POST":
        # Modifico #
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid():
        
            informacion= miFormulario.cleaned_data

            usuario.email= informacion['email']
            password= informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request, "inicio.html")

    else:
        miFormulario= UserEditForm(initial={'email':usuario.email})
        
    return render (request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


# def lista_pacientes(request):                   #función configurada en clase 18 HORA 1:48#
#    pacientes= Pacientes.objects.all()
#   datos= {"datos" : pacientes }
#    plantilla= loader.get_template("plantillas.html")
#   documento= plantilla.render(datos)
#   return HttpResponse(documento)

# def lista_prestadores(request):
#    prestadores= Prestadores.objects.all()
#    return HttpResponse (prestadores)

# def lista_proveedores(request):
#    proveedores= Proveedores.objects.all()
#    return HttpResponse (proveedores)
    
#  FALTA CONFIGURAR INGRESO POR FORMULARIO #
# def alta_pacientes (request):
#    paciente= Pacientes(nombre="María Laura Perez", edad=30, dni=38555678,  patologia="diabetes", talla=170, peso=70, contorno=80)
#    paciente.save()
#   paciente= Pacientes(nombre="Pedro Gutierrez", edad=67, dni=8577087,  patologia="diabetes", talla=180, peso=110, contorno=140)
#   paciente.save()
    
#    return HttpResponse("Se ha cargado lista de pacientes")

