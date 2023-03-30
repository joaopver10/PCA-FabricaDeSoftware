from django.urls import path

from .views import professor, aluno, matematica, ciencias, geografia, historia, portugues, ingles, portal

urlpatterns=[
    path('', portal, name='portal'),
    path('professor/', professor, name='professor'),
    path('aluno/', aluno, name='aluno'),
    path('matematica/', matematica, name='matematica'),
    path('ciencias/', ciencias, name='ciencias'),
    path('geografia/', geografia, name='geografia'),
    path('historia/', historia, name='historia'),
    path('portugues/', portugues, name='portugues'),
    path('ingles/', ingles, name='ingles')


]