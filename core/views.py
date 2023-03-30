from django.shortcuts import render


def professor(request):
    return render(request, 'professor.html')


def aluno(request):
    return render(request, 'aluno.html')


def portal(request):
    return render(request, 'portal.html')


def matematica(request):
    return render(request, 'matematica.html')


def ingles(request):
    return render(request, 'ingles.html')


def geografia(request):
    return render(request, 'geografia.html')


def historia(request):
    return render(request, 'historia.html')


def portugues(request):
    return render(request, 'portugues.html')


def ciencias(request):
    return render(request, 'ciencias.html')