

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render


def index(request):
    ahora = datetime.now()
    dia = ahora.strftime("%A %d de %B de %Y")
    hora = ahora.strftime("%H:%M:%S")
    return render(request, "index.html", {"dia": dia, "hora": hora})