def index(request):
    ahora = datetime.datetime.now()
    dia = ahora.strftime("%A %d de %B de %Y")
    hora = ahora.strftime("%H:%M:%S")
    return render(request, "index.html", {"dia": dia, "hora": hora})