from django.urls import path

from .views import professor, aluno, matematica, ciencias, geografia, historia, portugues, ingles, portal, sair, painel

urlpatterns=[
    path('', aluno, name='aluno'),
    path('portal/', portal, name='portal'),
    path('professor/', professor, name='professor'),
    path('matematica/', matematica, name='matematica'),
    path('ciencias/', ciencias, name='ciencias'),
    path('geografia/', geografia, name='geografia'),
    path('historia/', historia, name='historia'),
    path('portugues/', portugues, name='portugues'),
    path('ingles/', ingles, name='ingles'),
    path('painel/', painel, name='painel'),
    path('deslogar', sair, name='sair')

]