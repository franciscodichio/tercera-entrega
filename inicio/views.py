

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from inicio.models import Animal


def mi_vista(request):
    return HttpResponse('<h1>mi vista</h1>')

def mi_primer_template(request):
    
    archivo = open(r'C:\Users\Luciana\Desktop\tercera entrega\tercera-entrega\proyecto_django\mi_primer_template.html')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def mostrar_fecha(request):
    # dt = datetime.now()
    # dt_formateado = dt.strftime("%A %d %B %Y %T :%M")
    # return HttpResponse(dt_formateado)
    
    archivo = open(r'C:\Users\Luciana\Desktop\tercera entrega\tercera-entrega\proyecto_django\mostrar_fecha.html')
    
    template2 = Template(archivo.read())
    
    archivo.close()
    
    contexto2 = Context()
    
    template_renderizado2 = template2.render(contexto2)
    
    return HttpResponse(template_renderizado2)


from django.shortcuts import render
import datetime

def index(request):
    ahora = datetime.datetime.now()
    dia = ahora.strftime("%A %d de %B de %Y")
    hora = ahora.strftime("%H:%M:%S")
    return render(request, "index.html", {"dia": dia, "hora": hora})


def crear_animal(request):
    animal = Animal('Angelito', 3)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    datos = {'animal': animal}
    template = loader.get_template(r'crear animal')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)


def prueba_template(request):
    datos = {
        'nombre' : 'lionel',
        'apellido' : 'messi',
        'anios' : [
            1990, 2001, 2003, 2010, 2014
        ]
    }
    
    template = loader.get_template(r'mi_primer_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)



from django.shortcuts import render, redirect
from .forms import AnimalForm

def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(crear_animal)
    else:
        form = AnimalForm()
    return render(request, 'crear_animal.html', {'form':form})

    
