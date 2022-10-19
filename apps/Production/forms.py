# |----- Importación de librerías -----|
from cProfile import label
from django import forms # Se importan los formularios de Django
from .models import * # Se importa el modelo Employee del archivo models.py
from django.contrib.auth.models import User

class assistenceForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs.update({
            "type":"text",
            "placeholder":"Ingrese su Id de empleado",
            "class": "form-control form-control-md"
            })
  
    # class Meta: Se utiliza para definir los atributos de la clase "stadiumForm".
    class Meta:
        model = User # Se indica el modelo al que pertenece el formulario
        # Se definen los campos que se mostrarán en el formulario
        fields = [
            'id'] # Se definen los campos que se mostrarán en el formulario