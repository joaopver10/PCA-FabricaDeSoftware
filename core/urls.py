from django.urls import path, include

from .views import professor, aluno, matematica, ciencias, geografia,\
    historia, portugues, ingles, portal, sair, painel, quiz,\
    QuizListView, quiz_data_view, save_quiz_view

urlpatterns=[
    path('', aluno, name='aluno'),
    path('portal', portal, name='portal'),
    path('professor', professor, name='professor'),
    path('matematica', matematica, name='matematica'),
    path('ciencias', ciencias, name='ciencias'),
    path('geografia', geografia, name='geografia'),
    path('historia', historia, name='historia'),
    path('portugues', portugues, name='portugues'),
    path('ingles', ingles, name='ingles'),
    path('painel', painel, name='painel'),
    path('deslogar', sair ,name='sair'),
    path('quiz/', QuizListView.as_view(), name='quiz'),
    path('quiz/<pk>/', quiz, name='quiz-view'),
    path('quiz/<pk>/save/', save_quiz_view, name='save-view'),
    path('quiz/<pk>/data/', quiz_data_view, name='quiz-data-view')

]