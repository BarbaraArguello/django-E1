from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def plantilla_index(request):
    #cargador de plantilla> loader
    plantilla = loader.get_template('index.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def plantilla_login(request):
    return render(request, 'login.html')