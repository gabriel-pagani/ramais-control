from .models import Ramais
from django.http import JsonResponse
from django.shortcuts import render


def home_view(request):
    return render(request, 'main.html')


def ramais_json(request):
    dados = list(Ramais.objects.values('nome', 'ramal', 'setor', 'maquina'))
    return JsonResponse(dados, safe=False)
