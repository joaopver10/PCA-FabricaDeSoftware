from django.urls import path, include

from .views import professor, aluno, matematica, ciencias, geografia,\
    historia, portugues, ingles, portal, sair, painel, quiz, cadastraQuiz, cadastraResposta, cadastraQuestao,\
    QuizListViewM, QuizListViewG, QuizListViewI, QuizListViewC, QuizListViewH,QuizListViewP,  quiz_data_view, save_quiz_view

urlpatterns=[
    path('aluno', aluno, name='aluno'),
    path('', portal, name='portal'),
    path('professor', professor, name='professor'),
    path('matematica', matematica, name='matematica'),
    path('ciencias', ciencias, name='ciencias'),
    path('geografia', geografia, name='geografia'),
    path('historia', historia, name='historia'),
    path('portugues', portugues, name='portugues'),
    path('ingles', ingles, name='ingles'),
    path('painel', painel, name='painel'),
    path('cadastraQuiz', cadastraQuiz, name='cadastraQuiz'),
    path('cadastraResposta', cadastraResposta, name='cadastraResposta'),
    path('cadastraQuestao', cadastraQuestao, name='cadastraQuestao'),
    path('deslogar', sair,name='sair'),
    path('quizMatematica/', QuizListViewM.as_view(), name='quizM'),
    path('quizGeografia/', QuizListViewG.as_view(), name='quizG'),
    path('quizIngles/', QuizListViewI.as_view(), name='quizI'),
    path('quizCiencias/', QuizListViewC.as_view(), name='quizC'),
    path('quizHistoria/', QuizListViewH.as_view(), name='quizH'),
    path('quizPortugues/', QuizListViewP.as_view(), name='quizP'),
    path('quizMatematica/<pk>/', quiz, name='quiz-view'),
    path('quizMatematica/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizMatematica/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizGeografia/<pk>/', quiz, name='quiz-view'),
    path('quizGeografia/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizGeografia/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizIngles/<pk>/', quiz, name='quiz-view'),
    path('quizIngles/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizIngles/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizCiencias/<pk>/', quiz, name='quiz-view'),
    path('quizCiencias/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizCiencias/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizHistoria/<pk>/', quiz, name='quiz-view'),
    path('quizHistoria/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizHistoria/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizPortugues/<pk>/', quiz, name='quiz-view'),
    path('quizPortugues/<pk>/save/', save_quiz_view, name='save-view'),
    path('quizPortugues/<pk>/data/', quiz_data_view, name='quiz-data-view')

]