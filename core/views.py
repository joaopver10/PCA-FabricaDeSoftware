from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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

    if User.objects.filter(id=request.user.id).first().is_teacher is False:
       return redirect('/')

    if request.method == 'POST':
        try:

            User = get_user_model()
            novo_aluno = Aluno()

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


def cadastraQuiz(request):
    if request.method == 'POST':
        try:
            novo_quiz = Quiz()
            novo_quiz.nome = request.POST.get('nome')
            novo_quiz.topico = request.POST.get('topico')
            novo_quiz.num_de_questoes = request.POST.get('qtd')
            novo_quiz.tempo = request.POST.get('tempo')
            novo_quiz.materia_id = request.POST.get('materia')
            novo_quiz.dificuldade = request.POST.get('dificuldade')
            novo_quiz.pts_necessarios = request.POST.get('pts')

            novo_quiz.save()

            messages.add_message(request, constants.SUCCESS, 'Quiz criado com sucesso.')
        except:
            messages.add_message(request, constants.ERROR, 'Ocorreu algum erro, tente novamente em instantes...')


    return render(request, 'cadastraQuiz.html',)


def cadastraQuestao(request):
    nova_questao = Questoes()
    contexto = Quiz.objects.all()

    if request.method == 'POST':
        try:
            nova_questao.pergunta = request.POST.get('pergunta')
            nova_questao.quiz_id = request.POST.get('quiz')
            nova_questao.save()

            messages.add_message(request, constants.SUCCESS, 'Questão cadastrada com sucesso.')
        except:
            messages.add_message(request, constants.ERROR, 'Ocorreu algum erro, tente novamente em instantes...')
    return render(request, 'cadastraQuestao.html', {'contexto': contexto })

def cadastraResposta(request):
    contextoQ = Questoes.objects.all()
    nova_resp = Answer()
    nova_resp2 = Answer()
    nova_resp3 = Answer()
    nova_resp4 = Answer()

    if request.method == 'POST':
        try:
            nova_resp.questao_id = request.POST.get('questao')
            nova_resp2.questao_id = request.POST.get('questao')
            nova_resp3.questao_id = request.POST.get('questao')
            nova_resp4.questao_id = request.POST.get('questao')

            nova_resp.texto = request.POST.get('resposta')
            nova_resp2.texto = request.POST.get('resposta2')
            nova_resp3.texto = request.POST.get('resposta3')
            nova_resp4.texto = request.POST.get('resposta4')

            if request.POST.get('c1'):
                nova_resp.correto = request.POST.get('c1')

            if request.POST.get('c2'):
                nova_resp2.correto = request.POST.get('c2')

            if request.POST.get('c3'):
                nova_resp3.correto = request.POST.get('c3')

            if request.POST.get('c4'):
                nova_resp4.correto = request.POST.get('c4')

            nova_resp.save()
            nova_resp2.save()
            nova_resp3.save()
            nova_resp4.save()

            messages.add_message(request, constants.SUCCESS, 'Respostas cadastrada com sucesso.')
        except:
            messages.add_message(request, constants.ERROR, 'Ocorreu algum erro, tente novamente em instantes...')

    return render(request, 'cadastraResposta.html', {'contextoQ': contextoQ})

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
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)
    contextP = Resultado.objects.filter(usuario_id=Aluno.objects.filter(usuario_id=request.user.id).first().matricula)

    result = contextP.values('pontos').aggregate(sum_pontos=Sum('pontos'))

    totalPts = contextP.filter(usuario_id=Aluno.objects.filter(usuario_id=request.user.id).first().matricula).aggregate(total=Sum('pontos'))['total']
    totalPtsFormatado = round(totalPts, 2)




    if User.objects.filter(id=request.user.id).first().is_teacher is True:
       return redirect('painel')

    return render(request, 'portal.html',{'context': context, 'contextP': contextP, 'result': result})


def matematica(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
        return redirect('painel')

    return render(request, 'matematica.html',{'context': context} )


def ingles(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
       return redirect('painel')

    return render(request, 'ingles.html', {'context': context})


def geografia(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
        return redirect('painel')

    return render(request, 'geografia.html', {'context': context})


def historia(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
        return redirect('painel')

    return render(request, 'historia.html', {'context': context})


def portugues(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
        return redirect('painel')

    return render(request, 'portugues.html', {'context': context})


def ciencias(request):
    User = get_user_model()
    context = Aluno.objects.filter(usuario_id=request.user.id)

    if User.objects.filter(id=request.user.id).first().is_teacher is True:
        return redirect('painel')

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


