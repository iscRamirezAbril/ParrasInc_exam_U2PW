# |----- Importación de librerías -----|
from cProfile import label
from django import forms # Se importan los formularios de Django
from .models import * # Se importa el modelo Employee del archivo models.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class employeeForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "type":"text",
            "placeholder":"Ingrese su nombre",
            "class": "form-control form-control-lg"
            })
  
        self.fields['last_name'].widget.attrs.update({
            "type":"text",
            "placeholder":"Ingrese sus apellidos",
            "class": "form-control form-control-lg"
            })
  
        self.fields['username'].widget.attrs.update({
            "type":"email",
            "placeholder":"Ingrese su email",
            "class": "form-control form-control-lg"
            })
          
        self.fields['password1'].widget.attrs.update({
            "type":"password",
            "placeholder":"Escriba una contraseña",
            "class": "form-control form-control-lg"
            })
          
        self.fields['password2'].widget.attrs.update({
            "type":"password",
            "placeholder":"Confirme su contraseña",
            "class": "form-control form-control-lg"
            })
  
  
    # class Meta: Se utiliza para definir los atributos de la clase "stadiumForm".
    class Meta:
        model = User # Se indica el modelo al que pertenece el formulario
        # Se definen los campos que se mostrarán en el formulario
        fields = [
            'first_name', 
            'last_name', 
            'username',
            'password1', 
            'password2',] # Se definen los campos que se mostrarán en el formulario


class CheckClock (ModelForm):
    class Meta:
        model = Assistence
        fields = ('assistWorker',)
        widgets = {
            'assistWorker': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'background-color: #fff; border: 1px solid #ced4da; border-radius: .25rem; padding: .375rem .75rem; width: 100%;', 
                'placeholder': 'Ingrese su número de empleado'}),
        }
