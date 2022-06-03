from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def piloto(request):
    return render(request, 'piloto.html')
