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
from datetime import date, datetime


@login_required(login_url="professor")
def painel(request):
    User = get_user_model()
    novo_aluno = Aluno()
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            senha = request.POST.get('dataNasc')
            user = User.objects.create_user(
                email=email,
                password=senha,
                is_student=True
            )
            novo_aluno.nome = request.POST.get('nome')
            novo_aluno.sexo = request.POST.get('sexo')
            novo_aluno.email = request.POST.get('email')
            novo_aluno.dataNasc = request.POST.get('dataNasc')
            novo_aluno.localNasc = request.POST.get('localNasc')
            novo_aluno.nomeResponsavel = request.POST.get('nomeResponsavel')
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
            novo_aluno.usuario_id = User.objects.filter(email=request.POST.get('email')).first().id




            user.save()
            novo_aluno.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')

        except:
            messages.add_message(request, constants.ERROR, 'Esse aluno já esta cadastrado')

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
    User = get_user_model()
    if request.method == 'POST':
        try:
            matricula = request.POST['matricula']
            senha = request.POST['dt_nascimento']
            fk_tabela2 = Aluno.objects.filter(matricula=matricula).first().usuario_id
            pk_tabela1 = User.objects.filter(id=fk_tabela2).first().id


            if (pk_tabela1 == fk_tabela2):
                email_tabela = User.objects.filter(id=fk_tabela2).first().email
                user = authenticate(request, username=email_tabela, password=senha)
                if user:
                        lg(request, user)
                        return redirect('portal')
                messages.error(request, 'E-mail ou senha inválida', extra_tags='login')
        except:
            messages.error(request, 'E-mail ou senha inválida', extra_tags='login')
            return render(request, 'aluno.html')


    return render(request, 'aluno.html')


@login_required(login_url="aluno")
def portal(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    print(context)

    return render(request, 'portal.html',{'context': context})


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
    return HttpResponseRedirect('/')