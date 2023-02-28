from django.shortcuts import render


def cadastro(request):
    return render(request, 'cadastro.html')

def quiz(request):
    return render(request, 'quiz.html')