from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from .models import Aluno, Professor

def professor(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = User.objects.get(email=email).username
            senha = request.POST['senha']
            user = authenticate(request, username=username, password=senha)
            if user:
                lg(request, user)
                return redirect('portal')
        except:
            messages.error(request, 'Email ou senha inválida', extra_tags='login')
            return redirect('aluno')

    return render(request, 'professor.html')

def aluno(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = User.objects.get(email=email).username
            senha = request.POST['senha']
            user = authenticate(request, username=username, password=senha)
            if user:
                lg(request, user)
                return redirect('portal')
        except:
            messages.error(request, 'Email ou senha inválida', extra_tags='login')
            return redirect('aluno')

    return render(request, 'aluno.html')


@login_required(login_url="aluno")
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

def sair(request):
    logout(request)
    return HttpResponseRedirect('aluno')
