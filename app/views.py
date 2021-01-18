from .models import Tarefas
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def lista(request):
    trfs = Tarefas.objects.filter(data_de_nascimento__lte = timezone.now()).order_by('data_de_nascimento')
    return render(request, 'front/list.html', {'trfs':trfs})


def helloWorld(request):
    return HttpResponse('Hello World!')


def tarefa(request, task):
    return render(request, 'front/inserir_tarefas.html', {'task':task})

