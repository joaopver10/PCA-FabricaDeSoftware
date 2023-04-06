from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from .models import Aluno, Professor, CustomUsuario
from .forms import CadastroModelAluno
from django.contrib.messages import constants

@login_required(login_url="professor")
def painel(request):
    if str(request.method) == 'POST':
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            sexo = request.POST.get('sexo')
            dataNasc = request.POST.get('dataNasc')
            localNasc = request.POST.get('localNasc')
            nomePai = request.POST.get('nomePai')
            nomeMae = request.POST.get('nomeMae')
            tel = request.POST.get('tel')
            cep = request.POST.get('cep')
            logr = request.POST.get('logr')
            uf = request.POST.get('uf')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            complemento = request.POST.get('complemento')
            turma = request.POST.get('turma')
            turno = request.POST.get('turno')
            ano = request.POST.get('ano')
            print(nome, email, senha, sexo, localNasc, dataNasc, nomePai, nomeMae, tel, cep,
                  logr, numero, bairro, uf,cidade, complemento, turma, turno, ano)

            if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(sexo.strip()) == 0 or \
                    len(dataNasc.strip()) == 0 or len(localNasc.strip()) == 0 or len(nomeMae.strip()) == 0 or \
                    len(nomePai.strip()) == 0 or len(tel.strip()) == 0 or len(cep.strip()) == 0 or len(logr.strip()) == 0 or\
                    len(numero.strip()) == 0 or len(cidade.strip()) == 0 or len(bairro.strip()) == 0 or len(uf.strip()) == 0 or\
                    len(complemento.strip()) == 0 or len(turma.strip()) == 0 or len(turno.strip()) == 0 or len(ano.strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')

                user = CustomUsuario.objects.create_user(
                    username = nome,
                    email = email,
                    password = senha,
                    sexo = sexo,
                    dataNasc = dataNasc,
                    localNasc = localNasc,
                    nomeMae = nomeMae,
                    nomePai = nomePai,
                    logr = logr,
                    uf = uf,
                    cidade = cidade,
                    bairro = bairro,
                    tel = tel,
                    cep = cep,
                    numero = numero,
                    complemento = complemento,
                    turma = turma,
                    turno = turno,
                    ano = ano,
                )
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
                return render(request, 'painel.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema.')
            return render(request, 'painel.html')
    return render(request, 'painel.html')



def professor(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = CustomUsuario.objects.get(email=email).username
            senha = request.POST['senha']
            user = authenticate(request, username=username, password=senha)
            print(email, senha, username)
            if user:
                lg(request, user)
                return redirect('painel')
        except:
            messages.error(request, 'Email ou senha inválida', extra_tags='login')
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
