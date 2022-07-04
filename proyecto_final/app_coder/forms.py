from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Formulario_pacientes(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad= forms.IntegerField()
    dni= forms.IntegerField()
    telefono= forms.IntegerField()
    email= forms.EmailField()
    
class Formulario_prestadores(forms.Form):
    nombre = forms.CharField(max_length=40)
    especialidad= forms.CharField(max_length=40)
    telefono= forms.IntegerField()
    email= forms.EmailField()

class Formulario_proveedores(forms.Form):
    nombre = forms.CharField(max_length=40)
    cuit= forms.IntegerField()
    cbu= forms.IntegerField()    
    telefono= forms.IntegerField()
    email= forms.EmailField()

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Ingrese email")
    password1= forms.CharField(label='Nueva contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput)

    class Meta: #para asociar a tabla#
        model= User
        fields= ['email', 'password1', 'password2']
        help_text= {k:"" for k in fields} 

