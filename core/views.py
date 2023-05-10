from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from .models import Aluno, Professor, Quiz, Questoes, Resultado,Answer
from django.contrib.auth import get_user_model
from django.contrib.messages import constants



class QuizListViewM(ListView):
    model = Quiz
    template_name = 'mainQuizM.html'


class QuizListViewG(ListView):
    model = Quiz
    template_name = 'mainQuizG.html'

class QuizListViewI(ListView):
    model = Quiz
    template_name = 'mainQuizI.html'

class QuizListViewP(ListView):
    model = Quiz
    template_name = 'mainQuizP.html'

class QuizListViewH(ListView):
    model = Quiz
    template_name = 'mainQuizH.html'

class QuizListViewC(ListView):
    model = Quiz
    template_name = 'mainQuizC.html'

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

    return render(request, 'portal.html',{'context': context})


def matematica(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'matematica.html',{'context': context} )


def ingles(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'ingles.html', {'context': context})


def geografia(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'geografia.html', {'context': context})


def historia(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'historia.html', {'context': context})


def portugues(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'portugues.html', {'context': context})


def ciencias(request):
    context = Aluno.objects.filter(usuario_id=request.user.id)
    return render(request, 'ciencias.html', {'context': context})


def quiz(request, pk):
    quiz = Quiz.objects.get(pk= pk)

    return render(request, 'quiz.html', {'obj': quiz})

@login_required(login_url="aluno")
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk= pk)
    questoes = []

    for q in quiz.get_questions():
        respostas = []
        for a in q.get_answers():
            respostas.append(a.texto)
        questoes.append({str(q): respostas})
    return JsonResponse({
        'data': questoes,
        'tempo': quiz.tempo
    })

@login_required(login_url="aluno")
def save_quiz_view(request, pk):
    resultado = Resultado()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Questoes.objects.get(pergunta=k)
            questions.append(question)

        user = Aluno.objects.filter(usuario_id=request.user.id).first().matricula
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.num_de_questoes
        results = []
        resp_correta = None

        for q in questions:
            a_selected = request.POST.get(q.pergunta)

            if a_selected != "":
                questions_answers = Answer.objects.filter(questao=q)
                for a in questions_answers:
                    if a_selected == a.texto:
                        if a.correto:
                            score += 1
                            resp_correta = a.texto
                    else:
                        if a.correto:
                            resp_correta = a.texto

                results.append({str(q): {'resp_correta': resp_correta, 'respondido': a_selected}})
            else:
                results.append({str(q): 'Não respondido'})

        score_ = score * multiplier

        resultado.quiz_id = quiz.id
        resultado.usuario_id = user
        resultado.pontos = score_

        resultado.save()

        if score_ >= quiz.pts_necessarios:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False,'score': score_, 'results': results})




    return JsonResponse({'text': 'works'})

def sair(request):
    logout(request)
    return HttpResponseRedirect('/')