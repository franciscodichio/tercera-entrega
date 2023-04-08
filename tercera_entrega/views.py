from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def mi_vista(request):
    return HttpResponse('<h1>mi vista</h1>')

def mi_primer_template(request):
    
    archivo = open(r'C:\Users\Luciana\Desktop\tercera entrega\tercera-entrega\proyecto_django\mi_primer_template.html')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)