from django.shortcuts import render
from . import utils

def home(request):
    respuesta = None
    parametros = request.GET.get('parametros')
    if 'newton' in request.GET:
        respuesta  = utils.newton(parametros)
    return render(request,'home.html',{'respuesta':respuesta})

