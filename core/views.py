from django.shortcuts import render
from django.contrib import messages
from core.forms import PilotoModelForm
from core.models import Piloto


def index(request):
    context = {
        'pilotos': Piloto.objects.all()
    }
    return render(request, 'index.html', context)


def piloto(request):
    if str(request.method) == 'POST':
        form = PilotoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto salvo com sucesso')
            form = PilotoModelForm()
        else:
            messages.error(request, 'Erro ao salvar piloto')

    else:
        form = PilotoModelForm()

    context = {
        'form': form
    }

    return render(request, 'piloto.html', context)
