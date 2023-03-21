from django.shortcuts import render


def cadastro(request):
    return render(request, 'cadastro.html')

def aluno(request):
    return render(request, 'aluno.html')

