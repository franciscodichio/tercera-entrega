# from django import forms
# from .models import Animal


# class AnimalForm(forms.ModelForm):
#     class Meta:
#         model = Animal
#         fields = ['nombre','edad']
        
        
from django import forms


class Animal(forms.Form):

    #Especificar los campos
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()


class persona(forms.Form):   
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    fecha_nacimiento= forms.DateField()
    
    



class auto(forms.Form):   
    marca= forms.CharField(max_length=15)
    velocidad= forms.IntegerField()
    fecha_creacion= forms.DateField()

# class DatosPersonales(forms.Form):   
#     direccion= forms.CharField(max_length=30)
#     telefono= forms.CharField(max_length=30)
#     email= forms.EmailField()

# class Usuario(forms.Form):   
#     nombre= forms.CharField(max_length=30)
#     apellido= forms.CharField(max_length=30)
#     dni= forms.CharField()
    