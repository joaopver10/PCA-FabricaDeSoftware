from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from .models import Aluno, Professor, CustomUsuario
from django.contrib.auth import get_user_model
from django.contrib.messages import constants



@login_required(login_url="professor")
def painel(request):
    novo_aluno = Aluno()
    if request.method == 'POST':
        try:
            novo_aluno.nome = request.POST.get('nome')
            novo_aluno.sexo = request.POST.get('sexo')
            novo_aluno.dataNasc = request.POST.get('dataNasc')
            novo_aluno.localNasc = request.POST.get('localNasc')
            novo_aluno.nomePai = request.POST.get('nomePai')
            novo_aluno.nomeMae = request.POST.get('nomeMae')
            novo_aluno.tel = request.POST.get('tel')
            novo_aluno.cep = request.POST.get('cep')
            novo_aluno.logr = request.POST.get('logr')
            novo_aluno.uf = request.POST.get('uf')
            novo_aluno.numero = request.POST.get('numero')
            novo_aluno.bairro = request.POST.get('bairro')
            novo_aluno.cidade = request.POST.get('cidade')
            novo_aluno.complemento = request.POST.get('complemento')
            novo_aluno.turma = request.POST.get('turma')
            novo_aluno.turno = request.POST.get('turno')
            novo_aluno.ano = request.POST.get('ano')
            novo_aluno.professor_id = Professor.objects.filter(usuario_id=request.user.id).first().id
            novo_aluno.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
            return render(request, 'painel.html')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema.')
            return render(request, 'painel.html')
    return render(request, 'painel.html')



def professor(request):
    User = get_user_model()
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = Professor.objects.get(email=email).email
            senha = request.POST['senha']
            pk_tabela1 = User.objects.filter(email=email).first().id
            fk_tabela2 = Professor.objects.filter(email=email).first().usuario_id

            if( pk_tabela1 == fk_tabela2 ):
                user = authenticate(request, email=username, password=senha)
                if user:
                    lg(request, user)
                    return redirect('painel')
                messages.error(request, 'E-mail ou senha inválida', extra_tags='login')
        except:
            messages.error(request, 'E-mail ou senha inválida', extra_tags='login')
            return redirect('professor')

    return render(request, 'professor.html')


def aluno(request):
    if request.method == 'POST':
        id = request.POST['matricula']
        username = User.objects.get(id=id).username
        dt_nascimento = request.POST['dt_nascimento']
        senha = User.objects.get(password=dt_nascimento).password
        user = authenticate(request, username=username, password=senha)
        if user:
                lg(request, user)
                return redirect('portal')

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
